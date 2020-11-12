import requests
from bs4 import BeautifulSoup
import csv
from collections import OrderedDict

URL = 'https://www.serebii.net/pokemon/all.shtml'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

content = soup.find(id='content')
data = content.find_all('td', {'class': 'fooinfo'})

# with open("log.csv", "w", encoding='utf-8') as output:
#     for data in alldata:
#         print(data.text.strip())
#         output.write(data.text.strip("\n") + ',')


with open("data2.csv", "w", newline='', encoding='utf-8') as output:
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



#p_numbers = content.find_all('span', {'class': 'infocard-cell-data', 'class': 'cell-name'})


# Write CSV file
# f = csv.writer(open("data.csv", "w", encoding='utf-8'))
# f.writerow(['number', 'names'])

# with open("data.csv", "wt", encoding='utf-8') as log:
#     writer = csv.writer(log, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     # for data in alldata:
#     #     pokeName = data.find('a', href=True)
#     #     print(pokeName)
#     #     print('--------')
#     #     if(pokeName is not None and pokeName.text is not ''):
#     #         writer.writerow([pokeName.text])
#     #         print(pokeName.text)
#     for data in alldata:
#         print(data.text.strip('\n') + ',')
#         writer.writerow([data.text.strip()])




with open('log.csv') as in_file:
    with open('cleanData.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        for row in csv.reader(in_file):
            if any(field.strip() for field in row):
                writer.writerow(row)





#for data in alldata:
#    print(data.text.strip())
#print(content)

