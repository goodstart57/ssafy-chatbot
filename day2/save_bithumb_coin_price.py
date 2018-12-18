import bs4
import random
import requests
import webbrowser

bithumb_url = 'https://www.bithumb.com/'

response = requests.get(bithumb_url)
doc = bs4.BeautifulSoup(response.text, 'html.parser')

coin_dict = {}
coin_table = doc.select_one("#tableAsset")

for element in coin_table.select_one("#assetSelectBTC").find_all("option")[:5]:
    if element.text=="원화":
        pass
    else:
        coin_dict[element.text] = element.get_attribute_list('value')[0]
print(list(coin_dict.items()))
coin_price_file_path = "./data/coin_price.txt"
f = open(coin_price_file_path, 'w')
for coin_name in list(coin_dict.items()):
    print("{0} : {1}".format(coin_name[0], coin_table.select_one('#assetReal'+coin_name[1]).text))
    f.write("{0} : {1}\n".format(coin_name[0], coin_table.select_one('#assetReal'+coin_name[1]).text))
f.close()