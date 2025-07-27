# pip install requests beautifulsoup4 lxml

import requests
from bs4 import BeautifulSoup
import csv

def scrape_page(soup, quotes):
    # Retrieve all the quote <div> HTML element on the page
    quote_elements = soup.find_all("div", class_="quote")

    # Iterate over the list of quote elements and apply the scraping logic
    for quote_element in quote_elements:
        # Extract the text of the quote
        text = quote_element.find("span", class_="text").get_text(strip=True)
        # Extract the author of the quote
        author = quote_element.find("small", class_="author").get_text(strip=True)

        # Extract the tag <a> HTML elements related to the quote
        tag_elements = quote_element.select(".tags .tag")

        # Store the list of tag strings in a list
        tags = []
        for tag_element in tag_elements:
            tags.append(tag_element.get_text(strip=True))

        # Append a dictionary containing the scraped quote data
        quotes.append(
            {
                "text": text,
                "author": author,
                "tags": ", ".join(tags)  # Merge the tags into a "A, B, ..., Z" string
            }
        )

# The URL of the home page of the target website
base_url = "https://quotes.toscrape.com"
# Retrieve the target web page
page = requests.get(base_url)

# Parse the target web page with Beautiful Soup
soup = BeautifulSoup(page.text, "lxml")

# Where to store the scraped data
quotes = []

# Scrape the home page
scrape_page(soup, quotes)

# Get the "Next →" HTML element
next_li_element = soup.find("li", class_="next")

# If there is a next page to scrape
while next_li_element is not None:
    next_page_relative_url = next_li_element.find("a", href=True)["href"]

    # Get the new page
    page = requests.get(base_url + next_page_relative_url)

    # Parse the new page
    soup = BeautifulSoup(page.text, "lxml")

    # Scrape the new page
    scrape_page(soup, quotes)

    # Look for the "Next →" HTML element in the new page
    next_li_element = soup.find("li", class_="next")

# Open (or create) the CSV file and ensure it is properly closed afterward
with open("quotes.csv", "w", encoding="utf-8", newline="") as csv_file:
    writer = csv.writer(csv_file)

    # Write the header row
    writer.writerow(["Text", "Author", "Tags"])

    # Write each quote as a row
    for quote in quotes:
        writer.writerow(quote.values())