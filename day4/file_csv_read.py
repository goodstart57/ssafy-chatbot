import csv

f = open('ssapy1.csv', 'r', encoding='utf-8')
csv_reader = csv.reader(f, delimiter=',')
for row in csv_reader:
    print(row)
f.close()