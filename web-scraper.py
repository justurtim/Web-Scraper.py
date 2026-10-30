import csv
import requests
from bs4 import BeautifulSoup

# Target URL
URL = "https://toscrape.com"

# Send an HTTP request to the webpage
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all the quote blocks
    quote_elements = soup.find_all("div", class_="quote")

    # Open a CSV file to save the data
    with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author"])  # Header row

        # Extract and print text from each block
        for element in quote_elements:
            text = element.find("span", class_="text").text
            author = element.find("small", class_="author").text

            print(f'"{text}" — {author}\n')
            writer.writerow([text, author])

    print("Data successfully saved to 'quotes.csv'")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
