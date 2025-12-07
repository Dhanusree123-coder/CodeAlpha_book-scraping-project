import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
url = "http://books.toscrape.com/catalogue/page-1.html"

# Get HTML content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# List to store data
books = []

# Extract book details
for book in soup.select('article.product_pod'):
    title = book.h3.a['title']
    price = book.select_one('p.price_color').text
    books.append({"Title": title, "Price": price})

# Convert to DataFrame
df = pd.DataFrame(books)

# Save to CSV
df.to_csv("books.csv", index=False)
print("Data saved to books.csv")
