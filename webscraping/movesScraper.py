import requests
from bs4 import BeautifulSoup
import csv

# will have to change this URL for each different pokemon type (bug, dragon, etc.)
URL = 'https://www.serebii.net/attackdex-swsh/bug.shtml'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# current URL pokemon type
pokeType = 'Bug'

content = soup.find(id='content')

data = content.find_all(True, {'class': ['fooinfo', 'cen']})

for row in data:
    row = row.text.split('\n')
    non_empty_row = [line for line in row if line.strip() != '']
    strings_wo_empty_lines = ''
    for line in non_empty_row:
        strings_wo_empty_lines += line
        strings_wo_empty_lines = strings_wo_empty_lines.strip('\n') + ','

        print(line)

with open("moves.csv", "w", newline='', encoding='utf-8') as output:
    w = csv.writer(output, delimiter=':')
    w.writerow(['name', 'PP', 'power', 'accuracy', 'description', 'type'])
    counter = 0
    for row in data:
        row = row.text.split('\n')
        non_empty_row = [line for line in row if line.strip() != '']
        strings_wo_empty_lines = ''
        for line in non_empty_row:
            strings_wo_empty_lines += line
            strings_wo_empty_lines = strings_wo_empty_lines.strip('\r').strip('		') + ':'
            counter += 1
            counter %= 5
        if counter == 0:
            strings_wo_empty_lines += pokeType + '\n'
        output.writelines(strings_wo_empty_lines)