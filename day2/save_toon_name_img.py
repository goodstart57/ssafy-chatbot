from datetime import datetime
from bs4 import BeautifulSoup as bs

import random
import requests

weekday_dict = {
    -1:'sun',
    0:'mon',
    1:'tue',
    2:'wed',
    3:'thu',
    4:'fri',
    5:'sat',
    6:'sun',
}

ntoon_url = 'https://m.comic.naver.com/webtoon/weekday.nhn?week='+weekday_dict[datetime.now().weekday()-1]
response = requests.get(ntoon_url)
doc = bs(response.text, 'html.parser')

name_img_list = list(map(lambda x: (x.select_one('img')["alt"], x.select_one('img')["src"]) , doc.find_all('span', class_='im_br')))
for ni in name_img_list:
    print(ni)