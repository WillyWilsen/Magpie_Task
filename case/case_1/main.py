import scraper
import pandas as pd

csv_file_path = '2024_Q1 - Scraper Technical Test Resource - Tokopedia.csv'
df = pd.read_csv(csv_file_path)

keywords = df['keyword'].tolist()
num_pages = df['number_of_page'].tolist()

data = []

# Scraping
for keyword, num_page in zip(keywords, num_pages):
  print(f"Scraping {keyword} with {num_page} pages")
  data += scraper.scrape_tokopedia(keyword, num_page)

# Post Processing
print("Post Processing")
for i in range(len(data)):
  data[i]['Price'] = int(data[i]['Price'].replace('Rp', '').replace('.', '').strip())
  data[i]['Sales Count'] = int(data[i]['Sales Count'].replace('+', '').replace(' ', '').replace('terjual', '').replace('rb', '000').replace('jt', '000000').strip())
  data[i]['GMV Estimation'] = data[i]['Price'] * data[i]['Sales Count']

# Export to CSV
print("Exporting to CSV")
df = pd.DataFrame(data)
df = df[['Keyword', 'SKU Name', 'Price', 'Sales Count', 'GMV Estimation', 'Page']]
df.to_csv('output.csv', index=False)