from datetime import datetime, timedelta

import json
import requests
import random

'''
1등 : 6개 다 맞기
2등 : 5개 + 보너스
3등 : 5개
4등 : 4개
5등 : 3개
'''

lotto_drw_day = datetime.now()
lotto_drw_day = lotto_drw_day - timedelta(lotto_drw_day.weekday()+2)
lotto_num = lotto_drw_day - datetime(2002,12,7)
lotto_num = str(int(lotto_num.days/7)+1)

# 로또번호 가져오기
nanum_lotto_url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo="+lotto_num
response = requests.get(nanum_lotto_url, verify=False)
lotto_info = json.loads(response.text)
lotto_num = []
for i in range(1, 6):
    lotto_num.append(lotto_info['drwtNo'+str(i)])
bonus_num = lotto_info['bnusNo']
print('This lotto is No.{0}({1})'.format(lotto_info['drwNo'], lotto_info['drwNoDate']))
print("Correct lotto num is {0} and bonus num is {1}".format(lotto_num, bonus_num))
# 뽑기
my_lotto_num = random.sample(range(1, 46), 6)
print("My lotto num is {0}".format(my_lotto_num))
# 확인
correct_len = 6 - len(list(set(my_lotto_num) - set(lotto_num)))

my_lotto_rank = ""
if correct_len==6:
    my_lotto_rank = "1등"
elif correct_len==5:
    if bonus_num in my_lotto_num :
        my_lotto_rank = "2등"
    else:
        my_lotto_rank = "3등"
elif correct_len==4:
    my_lotto_rank = "4등"
elif correct_len==3:
    my_lotto_rank = "5등"
else:
    my_lotto_rank = "순위권 외"
print("My lotto rank is {0}.".format(my_lotto_rank))