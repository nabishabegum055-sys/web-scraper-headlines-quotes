import requests
from bs4 import BeautifulSoup
import json


URL = "https://quotes.toscrape.com/"


def scrape_quotes():
    print("\n========== WEB SCRAPER ==========")
    print("Connecting to website...")

    try:
        response = requests.get(URL, timeout=10)

        if response.status_code != 200:
            print("❌ Failed to access website.")
            return

        soup = BeautifulSoup(response.text, "html.parser")

        quotes = []

        for quote in soup.select(".quote"):
            text = quote.select_one(".text").get_text(strip=True)
            author = quote.select_one(".author").get_text(strip=True)

            quotes.append({
                "quote": text,
                "author": author
            })

        print(f"\n✅ Successfully extracted {len(quotes)} quotes.")

        with open("output.json", "w", encoding="utf-8") as file:
            json.dump(quotes, file, indent=4, ensure_ascii=False)

        print("📁 Data saved to output.json")

        print("\n========== EXTRACTED QUOTES ==========")

        for item in quotes[:5]:
            print("\nQuote:", item["quote"])
            print("Author:", item["author"])

    except requests.exceptions.RequestException as error:
        print("❌ Connection error:", error)

    except Exception as error:
        print("❌ Error:", error)


def main():
    scrape_quotes()


if __name__ == "__main__":
    main()