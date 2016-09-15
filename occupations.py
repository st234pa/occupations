import csv
import random

reader = csv.reader(open('occupations.csv', 'r'))
d = {}
for row in reader:
    k, v = row
    d[k] = v
  
def select():
    total = 0
    for k in d:
        total += d[k]
        if random.random() * total < d[k]:
            return d.keys(k)

print(select())
