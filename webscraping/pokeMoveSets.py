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
                   missingPoke.append([pokemon[10], pokemon[0]])
                   print(pokemon[0] + ' is missing!!!!!!!!!')
               for row in data:
                   output.writelines(pokemon[10] + ',' + pokemon[0] + ',' + row.text.strip() + '\n')
       print(missingPoke, sep=', ')


missingPoke = [['13', 'Weedle'], ['14', 'Kakuna'], ['15', 'Beedrill'], ['16', 'Pidgey'], ['17', 'Pidgeotto'],
 ['18', 'Pidgeot'], ['19', 'Rattata'], ['20', 'Raticate'], ['21', 'Spearow'], ['22', 'Fearow'],
 ['23', 'Ekans'], ['24', 'Arbok'], ['46', 'Paras'], ['47', 'Parasect'], ['48', 'Venonat'],
 ['49', 'Venomoth'], ['56', 'Mankey'], ['57', 'Primeape'], ['69', 'Bellsprout'], ['70', 'Weepinbell'],
 ['71', 'Victreebel'], ['74', 'Geodude'], ['75', 'Graveler'], ['76', 'Golem'], ['84', 'Doduo'],
 ['85', 'Dodrio'], ['86', 'Seel'], ['87', 'Dewgong'], ['88', 'Grimer'], ['89', 'Muk'], ['96', 'Drowzee'],
 ['97', 'Hypno'], ['100', 'Voltorb'], ['101', 'Electrode'], ['152', 'Chikorita'], ['153', 'Bayleef'],
 ['154', 'Meganium'], ['155', 'Cyndaquil'], ['156', 'Quilava'], ['157', 'Typhlosion'], ['158', 'Totodile'],
 ['159', 'Croconaw'], ['160', 'Feraligatr'], ['161', 'Sentret'], ['162', 'Furret'], ['165', 'Ledyba'],
 ['166', 'Ledian'], ['167', 'Spinarak'], ['168', 'Ariados'], ['179', 'Mareep'], ['180', 'Flaaffy'],
 ['181', 'Ampharos'], ['187', 'Hoppip'], ['188', 'Skiploom'], ['189', 'Jumpluff'], ['190', 'Aipom'],
 ['191', 'Sunkern'], ['192', 'Sunflora'], ['193', 'Yanma'], ['198', 'Murkrow'], ['200', 'Misdreavus'],
 ['201', 'Unown'], ['203', 'Girafarig'], ['204', 'Pineco'], ['205', 'Forretress'], ['207', 'Gligar'],
 ['209', 'Snubbull'], ['210', 'Granbull'], ['216', 'Teddiursa'], ['217', 'Ursaring'], ['218', 'Slugma'],
 ['219', 'Magcargo'], ['228', 'Houndour'], ['229', 'Houndoom'], ['231', 'Phanpy'], ['232', 'Donphan'],
 ['234', 'Stantler'], ['235', 'Smeargle'], ['261', 'Poochyena'], ['262', 'Mightyena'], ['265', 'Wurmple'],
 ['266', 'Silcoon'], ['267', 'Beautifly'], ['268', 'Cascoon'], ['269', 'Dustox'], ['276', 'Taillow'],
 ['277', 'Swellow'], ['283', 'Surskit'], ['284', 'Masquerain'], ['285', 'Shroomish'], ['286', 'Breloom'],
 ['287', 'Slakoth'], ['288', 'Vigoroth'], ['289', 'Slaking'], ['296', 'Makuhita'], ['297', 'Hariyama'],
 ['299', 'Nosepass'], ['300', 'Skitty'], ['301', 'Delcatty'], ['307', 'Meditite'], ['308', 'Medicham'],
 ['311', 'Plusle'], ['312', 'Minun'], ['313', 'Volbeat'], ['314', 'Illumise'], ['316', 'Gulpin'],
 ['317', 'Swalot'], ['322', 'Numel'], ['323', 'Camerupt'], ['325', 'Spoink'], ['326', 'Grumpig'],
 ['327', 'Spinda'], ['331', 'Cacnea'], ['332', 'Cacturne'], ['335', 'Zangoose'], ['336', 'Seviper'],
 ['351', 'Castform'], ['352', 'Kecleon'], ['353', 'Shuppet'], ['354', 'Banette'], ['357', 'Tropius'],
 ['358', 'Chimecho'], ['366', 'Clamperl'], ['367', 'Huntail'], ['368', 'Gorebyss'], ['370', 'Luvdisc'],
 ['386', 'Deoxys'], ['387', 'Turtwig'], ['388', 'Grotle'], ['389', 'Torterra'], ['390', 'Chimchar'],
 ['391', 'Monferno'], ['392', 'Infernape'], ['393', 'Piplup'], ['394', 'Prinplup'], ['395', 'Empoleon'],
 ['396', 'Starly'], ['397', 'Staravia'], ['398', 'Staraptor'], ['399', 'Bidoof'], ['400', 'Bibarel'],
 ['401', 'Kricketot'], ['402', 'Kricketune'], ['408', 'Cranidos'], ['409', 'Rampardos'], ['410', 'Shieldon'],
 ['411', 'Bastiodon'], ['412', 'Burmy'], ['413', 'Wormadam'], ['414', 'Mothim'], ['417', 'Pachirisu'],
 ['418', 'Buizel'], ['419', 'Floatzel'], ['424', 'Ambipom'], ['429', 'Mismagius'], ['430', 'Honchkrow'],
 ['431', 'Glameow'], ['432', 'Purugly'], ['433', 'Chingling'], ['441', 'Chatot'], ['455', 'Carnivine'],
 ['456', 'Finneon'], ['457', 'Lumineon'], ['469', 'Yanmega'], ['472', 'Gliscor'], ['476', 'Probopass'],
 ['489', 'Phione'], ['490', 'Manaphy'], ['491', 'Darkrai'], ['492', 'Shaymin'], ['493', 'Arceus'],
 ['495', 'Snivy'], ['496', 'Servine'], ['497', 'Serperior'], ['498', 'Tepig'], ['499', 'Pignite'],
 ['500', 'Emboar'], ['501', 'Oshawott'], ['502', 'Dewott'], ['503', 'Samurott'], ['504', 'Patrat'],
 ['505', 'Watchog'], ['511', 'Pansage'], ['512', 'Simisage'], ['513', 'Pansear'], ['514', 'Simisear'],
 ['515', 'Panpour'], ['516', 'Simipour'], ['522', 'Blitzle'], ['523', 'Zebstrika'], ['540', 'Sewaddle'],
 ['541', 'Swadloon'], ['542', 'Leavanny'], ['580', 'Ducklett'], ['581', 'Swanna'], ['585', 'Deerling'],
 ['586', 'Sawsbuck'], ['594', 'Alomomola'], ['602', 'Tynamo'], ['603', 'Eelektrik'], ['604', 'Eelektross'],
 ['648', 'Meloetta'], ['650', 'Chespin'], ['651', 'Quilladin'], ['652', 'Chesnaught'], ['653', 'Fennekin'],
 ['654', 'Braixen'], ['655', 'Delphox'], ['656', 'Froakie'], ['657', 'Frogadier'], ['658', 'Greninja'],
 ['664', 'Scatterbug'], ['665', 'Spewpa'], ['666', 'Vivillon'], ['667', 'Litleo'], ['668', 'Pyroar'],
 ['669', 'Flabebe'], ['670', 'Floette'], ['671', 'Florges'], ['672', 'Skiddo'], ['673', 'Gogoat'],
 ['676', 'Furfrou'], ['720', 'Hoopa'], ['731', 'Pikipek'], ['732', 'Trumbeak'], ['733', 'Toucannon'],
 ['734', 'Yungoos'], ['735', 'Gumshoos'], ['739', 'Crabrawler'], ['740', 'Crabominable'], ['741', 'Oricorio'],
 ['774', 'Minior'], ['775', 'Komala'], ['779', 'Bruxish']]

def secondPass():
    for pokemon in missingPoke:
        URL = 'https://pokemondb.net/pokedex/%s/moves/7' % pokemon[1]
        print(URL)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        content = soup.find(id='main')
        data = content.find_all('td', {'class': 'cell-name'})

        with open("pokemonMoveSets.csv", "a+", newline='', encoding='utf-8') as output:
            print('buffer')
            if len(data) == 0:
                print(pokemon[1] + ' is missing!!!!!!!!!')
            for row in data:
                output.writelines(pokemon[0] + ',' + pokemon[1] + ',' + row.text.strip() + '\n')

if __name__ == '__main__':
    pass
    # first webscraper. Only gets gen 8 and adds missing pokemon into a list
    # firstPass()
    # get missing pokemon by checking previous gens url links
    # secondPass()