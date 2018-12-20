import csv

f = open('ssapy1.csv', 'a', encoding='utf-8')
ssapy1 = csv.writer(f)
ssapy1.writerow(['JAESEO LEE', 'goodstart57@gmail.com', 'no', 'ssapy', 'statistics'])
f.close()