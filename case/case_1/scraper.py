import requests
from bs4 import BeautifulSoup

def scrape_tokopedia(keyword, num_page):
  base_url = f"https://www.tokopedia.com/search?q={keyword}"
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

  data = []

  for page in range(1, num_page + 1):
    base_url = f"{base_url}&page={page}"
    response = requests.get(base_url, headers=headers, timeout=10)

    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')

      elements = soup.find_all('div', class_='css-1asz3by')
      for element in elements:
        sku_name_element = element.find('div', class_='prd_link-product-name')
        price_element = element.find('div', class_='prd_link-product-price')
        sales_count_element = element.find('span', class_='prd_label-integrity')

        sku_name = sku_name_element.text.strip()
        price = price_element.text.strip()
        if (sales_count_element):
          sales_count = sales_count_element.text.strip()
        else:
          sales_count = '0 terjual'

        data.append({
          'Keyword': keyword,
          'SKU Name': sku_name,
          'Price': price,
          'Sales Count': sales_count,
          'Page': page
        })

  return data