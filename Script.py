import cloudscraper
from bs4 import BeautifulSoup
import json

data = {}
scraper = cloudscraper.create_scraper()

# Counter for assigning IDs to products
product_id = 1

for i in range(1, 5):
    req = scraper.get(f"https://www.pascalcoste-shopping.com/esthetique/fond-de-teint.html?p={i}")
    soup = BeautifulSoup(req.text, 'html.parser')

    titles = soup.find_all('h3')
    img = soup.find_all('img', class_='product-image-photo')
    brand = soup.find_all('div', class_='uk-grid uk-grid-small small-label uk-grid-divider uk-flex-center')
    price = soup.select(
        'div.uk-visible-product.uk-text-center > div.uk-grid.uk-grid-small.uk-prix-final.uk-margin-remove-top.uk-flex-center > div:nth-child(2) > span')
    url = soup.find_all('a', class_='product photo product-item-photo uk-text-center')

    for title, image, brand_div, price_span, product_link in zip(titles, img, brand, price, url):
        product_data = {
            'Name': title.text.strip(),
            'Price': price_span.text.split('€')[0].replace('\xa0', ''),
            'Brand': brand_div.select_one('div:nth-child(1)').text,
            'Image URL': image['data-amsrc'],
            'Product URL': product_link['href']
        }
        data[f'product_{product_id}'] = product_data
        product_id += 1

# Writing data to JSON file
with open('extracted_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

for d in data.items():
    print(d)