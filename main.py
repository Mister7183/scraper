import requests
from bs4 import BeautifulSoup
import csv

def get_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error fetching the webpage:", e)
        return None

def parse_webpage(html):
    data = []
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        # Modify the following lines to extract data from the specific website
        # For example, if you want to extract product names and prices from a table:
        for row in soup.select('table tr'):
            product_name = row.select_one('.product-name').text.strip()
            product_price = row.select_one('.product-price').text.strip()
            data.append({'Product Name': product_name, 'Product Price': product_price})
    return data

def save_to_csv(data, file_path):
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Product Name', 'Product Price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for item in data:
                writer.writerow(item)
        print(f"Data saved to {file_path} successfully!")
    except IOError as e:
        print("Error saving data to CSV:", e)

def main():
    # Replace 'https://example.com' with the URL of the website you want to scrape
    url = 'https://example.com'
    file_path = 'scraped_data.csv'
    
    html = get_webpage(url)
    if html:
        data = parse_webpage(html)
        if data:
            save_to_csv(data, file_path)

if __name__ == "__main__":
    main()
