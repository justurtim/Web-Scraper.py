import requests
from bs4 import BeautifulSoup

# Replace with the news URL you want to scrape
URL = "https://ycombinator.com"

# Provide a User-Agent to avoid getting blocked by basic bot detection
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

response = requests.get(URL, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # target specific elements (e.g., span with class 'titleline' on Hacker News)
    headlines = soup.find_all("span", class_="titleline")

    print(f"--- Top Headlines from {URL} ---")
    for index, headline in enumerate(headlines, 1):
        # Extract text from the anchor tag inside the span
        link = headline.find("a")
        if link:
            title = link.text
            url = link["href"]
            print(f"{index}. {title}")
            print(f"   Link: {url}\n")
else:
    print(f"Error fetching page: {response.status_code}")
