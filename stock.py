import urllib2
from bs4 import BeautifulSoup



quote_page = 'http://www.bloomberg.com/quote/SPX:IND'

page = urllib2.urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')


name_box = soup.find('h1', attrs={'class': 'name'})
price_box = soup.find("div", attrs={"class":"price"})



name = name_box.string
price = price_box.string

print(name + ": " + price)


import csv
from datetime import datetime


with open('index.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow([name, price, datetime.now()])