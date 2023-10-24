# random map 만들어줌.

import random

WIDTH = 18
HEIGHT = 9

lines = []
for i in range(HEIGHT):
    tmp = []
    for j in range(WIDTH):
        tmp.append(str(random.randint(1, 9)))
    lines.append(tmp)

import csv
with open('map.csv', 'w') as f:
    wr = csv.writer(f)
    for line in lines:
        wr.writerow(line)
