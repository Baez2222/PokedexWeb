import requests
from bs4 import BeautifulSoup
import csv

# this file adds the category attribute to moves table.
# it's an image in serebii but it does have a whole page where
# the moves are separated by category

# change URL depending on category (physical, special, other)
URL = 'https://www.serebii.net/attackdex-swsh/other.shtml'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

moveCat = 'Other'

content = soup.find(id='content')
data = content.find_all('td', {'class': 'fooinfo'})

for row in data:
    row = row.text.split('\n')
    non_empty_row = [line for line in row if line.strip() != '']
    strings_wo_empty_lines = ''
    for line in non_empty_row:
        strings_wo_empty_lines += line
        strings_wo_empty_lines = strings_wo_empty_lines.strip('\n') + ','

        print(line)

with open("movesCategory.csv", "a+", newline='', encoding='utf-8') as output:
    w = csv.writer(output, delimiter=',')
    w.writerow(['name', 'category'])
    counter = 0
    for row in data:
        row = row.text.split('\n')
        non_empty_row = [line for line in row if line.strip() != '']
        strings_wo_empty_lines = ''
        for line in non_empty_row:
            if(counter == 0):
                strings_wo_empty_lines += line
                strings_wo_empty_lines = strings_wo_empty_lines.strip('\r').strip('		') + ','
            counter += 1
            counter %= 2
        if counter == 1:
            strings_wo_empty_lines += moveCat + '\n'
        output.writelines(strings_wo_empty_lines)