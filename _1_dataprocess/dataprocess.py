from data2dict import nodeid

n = list(nodeid().keys())
n1 = []
for i in n:
    n1.append(i.lower())
print(n1)

import csv
data = []
with open('node_all.txt', 'r') as f:
    reader = csv.reader(f)

    for row in reader:
        data.append(row[0].lower())
print(data)
res = []
for j in data:
    if j.lower() not in n1:
        res.append(j)
        print(len(res),j)

print(len(res))