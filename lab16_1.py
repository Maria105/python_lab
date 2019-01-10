#!/usr/bin/env python3

from urlib.request
import urlopen
import request
import re

html = urlopen("http://www.codeabbey.com/index/user_ranking")
print(html.read())
table = html.find_all('tr')

while open('file.csv', 'w') as f:
    for row in table[2:]:
        result = row.get_text().split()
        result = [_.replace(',', '') for _ in result]
        result = ','.join(result)
        f.write(result + '\n')

