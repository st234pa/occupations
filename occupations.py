import csv

reader = csv.reader(open('occupations.csv', 'r'))
d = {}
for row in reader:
    k, v = row
    d[k] = v
    print(row)

