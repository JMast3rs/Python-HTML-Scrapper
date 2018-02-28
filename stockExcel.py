import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def getStocks(stock):
	quote_page = 'http://www.bloomberg.com/' + stock

	page = urllib2.urlopen(quote_page)

	soup = BeautifulSoup(page, 'html.parser')
	
	name_box = soup.find('h1', attrs={'class': 'name'})
	price_box = soup.find("div", attrs={"class":"price"})

	name = name_box.string
	price = price_box.string

	print(name + ": " + price)

	with open('stocks.csv', 'a') as csv_file:
		writer = csv.writer(csv_file)
		writer.writerow([name, price, datetime.now()])


quote_page = 'https://www.bloomberg.com/markets/stocks'

page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')


linksearch = soup.findAll(href=True)

for link in linksearch:
	if (link['href']).find("quote/") >= 0:
		print(link['href'])
		getStocks(str(link['href']))


