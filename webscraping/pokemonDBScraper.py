import requests
from bs4 import BeautifulSoup
import csv
from collections import OrderedDict

URL = 'https://www.serebii.net/pokemon/all.shtml'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

content = soup.find(id='content')
data = content.find_all('td', {'class': 'fooinfo'})


with open("data.csv", "w", newline='', encoding='utf-8') as output:
    w = csv.writer(output)
    w.writerow(['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9'])
    for row in data:
        row = row.text.split('\n')
        non_empty_row = [line for line in row if line.strip() != '']
        strings_wo_empty_lines = ''
        for line in non_empty_row:
            strings_wo_empty_lines += line
            strings_wo_empty_lines = strings_wo_empty_lines.strip('\n') + ','
        output.writelines(strings_wo_empty_lines)