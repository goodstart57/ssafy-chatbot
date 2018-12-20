import csv

f = open('ssapy1.csv', 'w', encoding='utf-8')
ssapy1 = csv.writer(f)
ssapy1.writerow(['name', 'email', 'phone', 'group', 'major'])
f.close()