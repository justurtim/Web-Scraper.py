# Simple Web Scraper (Python)

A lightweight, easy-to-use Python web scraper built with **BeautifulSoup** and **Requests** to extract quotes or news headlines from websites. It includes automated extraction, terminal formatting, and CSV data export capabilities.

## Features
* **Quote Extraction:** Pulls quotes and authors from dynamic block structures and saves them directly to a CSV file.
* **Headline Extraction:** Extracts news titles and source URLs using browser-mimicking headers.
* **Data Persistence:** Automatically exports scraped items into organized files for analysis.
* **Anti-Blocking Basics:** Implements custom `User-Agent` strings to handle standard server-side bot filtering.

## Prerequisites
Ensure you have Python 3.7 or higher installed on your system.

## Installation

1. **Clone or download** this repository to your local machine.
2. Open your terminal or command prompt and install the required dependencies:

```bash
pip install requests beautifulsoup4
```

## Usage

### 1. Scraping Quotes
Run the quote scraper script to fetch quotes from the sandbox site and export them to a local spreadsheet.
```bash
python quote_scraper.py
```
* **Output:** Displays the extracted quotes in your console and generates a `quotes.csv` file in the same directory.

### 2. Scraping News Headlines
Run the headline scraper script to pull live tech headlines and URLs.
```bash
python headline_scraper.py
```
* **Output:** Prints a numbered list of current top headlines along with their source hyperlinks directly to the console.

## Project Structure
```text
├── quote_scraper.py     # Script for scraping quotes and saving to CSV
├── headline_scraper.py  # Script for extracting live news headlines
├── README.md            # Project documentation
└── quotes.csv           # Generated output data (created after running)
```

## Best Practices & Legalities
When using this scraper or adapting it for other sites, remember to:
* **Check the `robots.txt` file:** Always append `/robots.txt` to a website's domain to see what paths scrapers are allowed to access.
* **Be respectful:** Avoid hitting servers too quickly. Consider adding `import time; time.sleep(1)` between requests if scraping multiple pages to prevent IP bans.
* **Handle JavaScript:** This tool relies on static HTML parsing. If a website requires user interactions or loads content dynamically via JavaScript, consider upgrading the backend engine to **Playwright** or **Selenium**.
