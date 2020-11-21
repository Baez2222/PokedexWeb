import requests
from bs4 import BeautifulSoup
import csv


# will have to change this URL for each different pokemon
def firstPass():
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


missingPoke = ['Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 'Raticate', 'Spearow',
 'Fearow', 'Ekans', 'Arbok', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Mankey', 'Primeape',
 'Bellsprout', 'Weepinbell', 'Victreebel', 'Geodude', 'Graveler', 'Golem', 'Doduo', 'Dodrio', 'Seel',
 'Dewgong', 'Grimer', 'Muk', 'Drowzee', 'Hypno', 'Voltorb', 'Electrode', 'Chikorita', 'Bayleef',
 'Meganium', 'Cyndaquil', 'Quilava', 'Typhlosion', 'Totodile', 'Croconaw', 'Feraligatr', 'Sentret',
 'Furret', 'Ledyba', 'Ledian', 'Spinarak', 'Ariados', 'Mareep', 'Flaaffy', 'Ampharos', 'Hoppip',
 'Skiploom', 'Jumpluff', 'Aipom', 'Sunkern', 'Sunflora', 'Yanma', 'Murkrow', 'Misdreavus', 'Unown',
 'Girafarig', 'Pineco', 'Forretress', 'Gligar', 'Snubbull', 'Granbull', 'Teddiursa', 'Ursaring',
 'Slugma', 'Magcargo', 'Houndour', 'Houndoom', 'Phanpy', 'Donphan', 'Stantler', 'Smeargle', 'Poochyena',
 'Mightyena', 'Wurmple', 'Silcoon', 'Beautifly', 'Cascoon', 'Dustox', 'Taillow', 'Swellow', 'Surskit',
 'Masquerain', 'Shroomish', 'Breloom', 'Slakoth', 'Vigoroth', 'Slaking', 'Makuhita', 'Hariyama',
 'Nosepass', 'Skitty', 'Delcatty', 'Meditite', 'Medicham', 'Plusle', 'Minun', 'Volbeat', 'Illumise',
 'Gulpin', 'Swalot', 'Numel', 'Camerupt', 'Spoink', 'Grumpig', 'Spinda', 'Cacnea', 'Cacturne',
 'Zangoose', 'Seviper', 'Castform', 'Kecleon', 'Shuppet', 'Banette', 'Tropius', 'Chimecho', 'Clamperl',
 'Huntail', 'Gorebyss', 'Luvdisc', 'Deoxys', 'Turtwig', 'Grotle', 'Torterra', 'Chimchar', 'Monferno',
 'Infernape', 'Piplup', 'Prinplup', 'Empoleon', 'Starly', 'Staravia', 'Staraptor', 'Bidoof', 'Bibarel',
 'Kricketot', 'Kricketune', 'Cranidos', 'Rampardos', 'Shieldon', 'Bastiodon', 'Burmy', 'Wormadam',
 'Mothim', 'Pachirisu', 'Buizel', 'Floatzel', 'Ambipom', 'Mismagius', 'Honchkrow', 'Glameow', 'Purugly',
 'Chingling', 'Chatot', 'Carnivine', 'Finneon', 'Lumineon', 'Yanmega', 'Gliscor', 'Probopass', 'Phione',
 'Manaphy', 'Darkrai', 'Shaymin', 'Arceus', 'Snivy', 'Servine', 'Serperior', 'Tepig', 'Pignite', 'Emboar',
 'Oshawott', 'Dewott', 'Samurott', 'Patrat', 'Watchog', 'Pansage', 'Simisage', 'Pansear', 'Simisear',
 'Panpour', 'Simipour', 'Blitzle', 'Zebstrika', 'Sewaddle', 'Swadloon', 'Leavanny', 'Ducklett', 'Swanna',
 'Deerling', 'Sawsbuck', 'Alomomola', 'Tynamo', 'Eelektrik', 'Eelektross', 'Meloetta', 'Chespin',
 'Quilladin', 'Chesnaught', 'Fennekin', 'Braixen', 'Delphox', 'Froakie', 'Frogadier', 'Greninja',
 'Scatterbug', 'Spewpa', 'Vivillon', 'Litleo', 'Pyroar', 'Flabebe', 'Floette', 'Florges', 'Skiddo',
 'Gogoat', 'Furfrou', 'Hoopa', 'Pikipek', 'Trumbeak', 'Toucannon', 'Yungoos', 'Gumshoos', 'Crabrawler',
 'Crabominable', 'Oricorio', 'Minior', 'Komala', 'Bruxish', 'Nidoran♀', 'Nidoran♂']

def secondPass():
    for pokemon in missingPoke:
        URL = 'https://pokemondb.net/pokedex/%s/moves/7' % pokemon
        print(URL)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        content = soup.find(id='main')
        data = content.find_all('td', {'class': 'cell-name'})

        with open("pokemonMoveSets.csv", "a+", newline='', encoding='utf-8') as output:
            if len(data) == 0:
                print(pokemon + ' is missing!!!!!!!!!')
            for row in data:
                output.writelines(pokemon + ',' + row.text.strip() + '\n')

if __name__ == '__main__':
    pass
    # first webscraper. Only gets gen 8 and adds missing pokemon into a list
    # firstPass()
    # get missing pokemon by checking previous gens url links
    # secondPass()