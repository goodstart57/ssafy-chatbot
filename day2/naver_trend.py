'''
1. requests에게 naver.com 요청을 보내서
2. 응답 받은 문서를 저장
3. BeautifuleSoup 정보를 찾기 좋게 만들기
4. 우리가 원하는 정보를 뽑기
'''

import bs4
import random
import requests
import time
import webbrowser

naver_url = 'https://www.naver.com'

response = requests.get(naver_url)
doc = bs4.BeautifulSoup(response.text, 'html.parser')

pop_keywords = list(map(lambda x: x.text, doc.select(".ah_k")))
pop_keywords = random.sample(pop_keywords, 3)

webbrowser.open_new('https://search.naver.com/search.naver?query='+pop_keywords[0])
print("'{0}'이(가) 검색되었습니다.".format(pop_keywords[0]))
time.sleep(0.5)
for pop_keyword in pop_keywords[1:]:
    webbrowser.open_new_tab('https://search.naver.com/search.naver?query='+pop_keyword)
    print("'{0}'이(가) 검색되었습니다.".format(pop_keyword))
    time.sleep(0.5)