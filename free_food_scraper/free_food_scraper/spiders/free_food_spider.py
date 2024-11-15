import scrapy
import re
import csv

URL_FILE_NAME = "urls.txt"

class FreeFoodSpider(scrapy.Spider):
    name = "free_food_spider"
    
    def __init__(self, *args, **kwargs):
        super(FreeFoodSpider, self).__init__(*args, **kwargs)
        # Open the CSV file and set up the writer
        self.results_file = open('results.csv', 'w', newline='', encoding='utf-8')
        self.csv_writer = csv.writer(self.results_file)
        # Write the header row
        #TODO: - this needs to be improved
        #self.csv_writer.writerow(['keyword', 'url', 'locations', 'times'])
        # for now, just have the keyword and the url
        self.csv_writer.writerow(['keyword', 'url'])

    def start_requests(self):
        with open(URL_FILE_NAME, "r") as file:
            urls = file.read().splitlines()
        
        for url in urls:
            if not url.startswith(('http://', 'https://')):
                self.logger.error(f"Invalid URL in file: {url}")
                continue
            print(f"Starting request for URL: {url}")
            yield scrapy.Request(url=url, callback=self.parse)

    WORDS = [
        "Food Pantry",
        "Food Bank",
        "Emergency Food",
        "Soup Kitchen",
        "Food Distribution"
    ]

    def parse(self, response):
        # Check if the response content is text-based
        content_type = response.headers.get('Content-Type', b'').decode('utf-8')
        if not content_type.startswith('text'):
            self.logger.warning(f"Non-text response received at {response.url}. Content-Type: {content_type}")
            return  # Skip processing if content is not text

        # Convert the response to lowercase for easier searching
        page_text = response.text.lower()

        for word in self.WORDS:
            if word.lower() in page_text:
                # Find time and location information
                time_pattern = r'\b(\d{1,2}:\d{2}\s*(am|pm)?)\b'
                location_pattern = r'\b(\d{1,5}\s+\w+\s+\w+\s+\w{2}\s+\d{5})\b'
                
                times = re.findall(time_pattern, response.text, re.IGNORECASE)
                locations = re.findall(location_pattern, response.text, re.IGNORECASE)

                times = [time[0] for time in times]
                locations = [location[0].strip() for location in locations]

                # Write the result directly to the CSV file
                # TODO: - This needs to be improved
                #self.csv_writer.writerow([word, response.url, '; '.join(times), '; '.join(locations)])
                # for now, just return the key word that was used and the url
                self.csv_writer.writerow([word, response.url])
                break
        
        # Extract sublinks on the page and crawl them
        sublinks = response.css("a::attr(href)").getall()
        for sublink in sublinks:
            full_url = response.urljoin(sublink)
            if not full_url.startswith(('http://', 'https://')):
                self.logger.warning(f"Invalid sublink found: {sublink}")
                continue

            yield scrapy.Request(url=full_url, callback=self.parse)

    def close(self, reason):
        self.results_file.close()
        self.logger.info(f"Results saved to results.csv")
