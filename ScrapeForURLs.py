from googlesearch import search


global KEYWORDS
KEYWORDS = [
        "Food Pantry",
        "Food Bank",
        "Emergency Food",
        "Soup Kitchen",
        "Food Distribution"
]

def search_for_urls(keywords, num_results=100):
    urls = []
    for i, keyword in enumerate(keywords):
        # clear terminal line
        print(" " * 100, end="\r")
        print("Searching for: ", keyword, "(", i+1, "/", len(keywords), ")", end="\r")
        for url in search(keyword, num_results=num_results):
            urls.append(url)
    return urls


if __name__ == "__main__":
    urls = search_for_urls(KEYWORDS)

    # write urls into a file
    OUTPUT_FILE = "free_food_scraper/urls.txt"
    with open(OUTPUT_FILE, "w") as f:
        for url in urls:
            f.write(url + "\n")