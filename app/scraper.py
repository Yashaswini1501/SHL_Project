import requests
from bs4 import BeautifulSoup
import json

url = "https://www.shl.com/solutions/products/product-catalog/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

assessments = []

cards = soup.find_all("a")

for card in cards:
    text = card.get_text(strip=True)

    href = card.get("href")

    if text and href:
        if "/products/" in href:

            assessment = {
                "name": text,
                "url": href if href.startswith("http") else "https://www.shl.com" + href,
                "description": text,
                "test_type": "Unknown"
            }

            assessments.append(assessment)

with open("data/catalog.json", "w") as f:
    json.dump(assessments, f, indent=4)

print("Catalog saved!")