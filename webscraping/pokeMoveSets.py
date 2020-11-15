import requests
from bs4 import BeautifulSoup
import csv


# will have to change this URL for each different pokemon
with open("pokedex_missingTypes.csv", "r", encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    missingPoke = []
    for pokemon in csv_reader:
        print(pokemon[0])
        # changes URL to get every pokemon
        URL = 'https://pokemondb.net/pokedex/%s/moves/8' % pokemon[0]
        print(URL)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        content = soup.find(id='main')
        data = content.find_all('td', {'class': 'cell-name'})

        with open("pokemonMoveSets.csv", "a+", newline='', encoding='utf-8') as output:
            if len(data) == 0:
                missingPoke.append(pokemon[0])
                print(pokemon[0] + ' is missing!!!!!!!!!')
            for row in data:
                output.writelines(pokemon[0] + ',' + row.text.strip() + '\n')
    print(missingPoke, sep=', ')