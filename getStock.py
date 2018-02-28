import urllib2
from bs4 import BeautifulSoup

stocklist = []

def getStocks(stock):
	quote_page = 'http://www.bloomberg.com/' + stock

	page = urllib2.urlopen(quote_page)

	soup = BeautifulSoup(page, 'html.parser')
	
	name_box = soup.find('h1', attrs={'class': 'name'})
	price_box = soup.find("div", attrs={"class":"price"})

	name = name_box.string
	price = price_box.string

	print(name + ": " + str(price))


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


urlList = ['https://www.bloomberg.com/markets/stocks/futures', 'https://www.bloomberg.com/markets/stocks', 'https://www.bloomberg.com/markets/regions/americas']

for urls in urlList:
	stocklist = getStockList(stocklist, urls)

for i in stocklist:
	getStocks(i)

print(len(stocklist))




