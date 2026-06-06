"""Extract UK Open Banking API performance data.

This script will download public Open Banking performance data and save the
original file in data/raw/. For now, it only defines the script purpose.
"""
import requests
from pathlib import Path


historic_csv_url = "https://www.openbanking.org.uk/wp-content/uploads/Historic-Data-Download-csv-28.csv"
output_path = Path("data/raw/open_banking_api_performance_historic.csv")

def download_csv(url):
    response = requests.get(url, timeout=30)
    print(response.status_code)
    return response.text


def save_csv(content, output_path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")

csv_content = download_csv(historic_csv_url)
save_csv(csv_content, output_path)
