# Free Food Map Scraper

A web scraper that searches for free food and meal resources or events online. The scraper follows URL links and their sub-links (if available) to find specified keywords and stores the data in a CSV file.

## Installation

1. **Clone the repository** or download the zip file.

2. **Install dependencies** by running:
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Find URLs by keywords**:
   To gather URLs for specific keywords, run:
   ```bash
   python3 ScrapeForUrls.py
   ```
   - This will create a file named `urls.txt` in the *free_food_scraper* directory with URLs related to the keywords, using [Google Search Results](https://github.com/Nv7-GitHub/googlesearch).

4. **Run the scraper**:
   To scrape data from the URLs generated in the previous step, run:
   ```bash
   scrapy crawl free_food_spider
   ```
   - **Note**: Make sure to be in the *free_food_scraper* directory to execute this command.

5. **Output**:
   - The scraper will generate a file called `results.csv` containing the scraped data. Each time the scraper runs, it appends new data to this file.
   - To stop the scraper, use the keyboard shortcut `Ctrl + C`. You may need to press it multiple times to halt all scraper threads.

## Configuration

- **Keywords for Google search** can be modified in `ScrapeForUrls.py`.
- **Data scraping keys** can be adjusted in `free_food_scraper.py`.

## TODOs

Tasks that still need to be completed:

- [x] Scrape the web for URLs using a set of keywords.
- [x] Scrape URLs and sub-URLs for the specified keywords.
- [x] Store data in a CSV file.
- [ ] Extract and properly format location and time information from the scraped data.

## Documentation & References

- [Google Search Results - GitHub](https://github.com/Nv7-GitHub/googlesearch)
- [Scrapy Python Documentation](https://docs.scrapy.org/en/latest/)
