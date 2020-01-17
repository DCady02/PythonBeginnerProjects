import requests
import csv
from bs4 import BeautifulSoup

def scrape_books(page_num):

	url = "http://books.toscrape.com/catalogue/page-" + str(page_num) + ".html"

	response = requests.get(url)

	soup = BeautifulSoup(response.text, 'html.parser')

	# h3 elements = book titles

	books = soup.find_all(class_='product_pod')

	print(books)

	for book in books:
		title = book.select("a")[1]['title']

		price = book.find(class_='price_color').get_text().replace('Â', '')

		# link = book.select("a")[1]['href']

		rating = book.select("p")[0].attrs['class'][1]

		csv_writer.writerow([title, rating, price])

x = 0

with open('books.csv', 'w') as csvfile:
	csv_writer = csv.writer(csvfile)
	headers = ['Title', 'Rating', 'Price']
	csv_writer.writerow(headers)

	for y in range(1, 50):
		scrape_books(x)
		x += y
