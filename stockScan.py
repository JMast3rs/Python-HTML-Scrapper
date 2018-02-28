
#Basic Function - finds links on a page and get the stock price from list.

import urllib2
from bs4 import BeautifulSoup

def addStock(stocklist, newstock):
	if newstock in stocklist:
		print("error")
		return stocklist
	return stocklist + [newstock]


def getStockList(stocklist, url):
	page = urllib2.urlopen(url)

	soup = BeautifulSoup(page, 'html.parser')

	linksearch = soup.findAll(href=True)

	for link in linksearch:
		if (link['href']).find("quote/") >= 0:
			stocklist = addStock(stocklist , str(link['href']).replace(" ","%20"))
	return stocklist


print(getStockList([], 'https://www.bloomberg.com/markets/stocks/futures'))