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

	return name, str(price)


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

nameList = []
priceList = []

for i in stocklist:
	name, price = getStocks(i)
	nameList += [name]
	priceList += [price]

print(len(stocklist))


f = open('index.html','w')

top = "<html><head></head><body><h1>Stocks!</h1>"

content = ""

for i in range(len(stocklist)):
	content += "<h3>" + nameList[i] + "</h3>" + priceList[i]

bottom = "</body></html>"

message = top + content + bottom

f.write(message)
f.close()


