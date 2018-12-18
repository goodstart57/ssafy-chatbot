import bs4
import random
import requests
import webbrowser

bithumb_url = 'https://www.bithumb.com/'

response = requests.get(bithumb_url)
doc = bs4.BeautifulSoup(response.text, 'html.parser')

res = doc.select_one('.coin_list').select('strong')

coin_price_file_path = "./data/coin_price.txt"
f = open(coin_price_file_path, 'w')
for i, strong in enumerate(res):
    if i%5==0:
        info = "{0} : ".format(strong.text)
    elif i%5==1:
        print(info + "{0}".format(strong.text))
        f.write(info + "{0}".format(strong.text))
    else:
        pass
f.close()