from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.webull.com/quote/crypto'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

coin_data = soup.findAll("div",attrs={"class":"table-cell"})
name_data = soup.findAll("p",attrs={"class": "tit bold"})

name_counter = 0
counter = 1
for x in range(5):
    name = name_data[name_counter].text
    current_price = float(coin_data[counter + 1].text.replace(',',''))
    change = float(coin_data[counter + 2].text.replace(',','').replace('%',''))
    prev_price = round((current_price / (1 + (change/100))),2)

    print(f"Company Name: {name}")
    print(f"Current Price: {current_price}")
    print(f"Change: {change}%")
    print(f"Previous Price: {prev_price}")

    name_counter += 1
    counter += 10

#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")
