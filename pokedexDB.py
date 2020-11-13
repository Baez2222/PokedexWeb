from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import csv


# populate pokemon table
def insert_pokemon(row):
    # input name,abilities1,abilities2,abilities3,hp,att,def,S-att,S-def,spd,no
    query = "INSERT INTO pokemon(pokeID,name,primaryType,secondaryType,description,ability1,ability2,ability3,hp,attack,defense,sp_attack,sp_defense,speed,region)" \
            "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    if row[2] == '':
        row[2] = None
    if row[3] == '':
        row[3] = None
    args = (row[10],row[0],None,None,None,row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],None)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()
    except Error as error:
        print(error)


def insert_types(row):
    typeDict = {
        '1': 'Normal',
        '2': 'Fighting',
        '3': 'Flying',
        '4': 'Poison',
        '5': 'Ground',
        '6': 'Rock',
        '7': 'Bug',
        '8': 'Ghost',
        '9': 'Steel',
        '10': 'Fire',
        '11': 'Water',
        '12': 'Grass',
        '13': 'Electric',
        '14': 'Psychic',
        '15': 'Ice',
        '16': 'Dragon',
        '17': 'Dark',
        '18': 'Fairy'
    }
    # input type using pokeID
    if row[2] == '1':
        query = "UPDATE pokemon SET primaryType = %s WHERE pokeID = %s"
    else:
        query = "UPDATE pokemon SET secondaryType = %s WHERE pokeID = %s"
    args = (typeDict[row[1]], row[0])

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    id = cursor.lastrowid


def insert_moves(row):
    # input name,abilities1,abilities2,abilities3,hp,att,def,S-att,S-def,spd,no
    query = "INSERT INTO moves(name,type,category,PP,power,accuracy,description)" \
            "VALUES(%s,%s,%s,%s,%s,%s,%s)"
    if row[2] == '--':
        row[2] = None
    if row[3] == '--':
        row[3] = None
    args = (row[0], row[5], None, row[1], row[2], row[3], row[4])

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()
    except Error as error:
        print(error)


def insert_movesCat(row):
    # input category using name (primary)
    query = "UPDATE moves SET category = %s WHERE name = %s"
    args = (row[1], row[0])

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        conn.commit()
    except Error as error:
        print(error)


def main():
    with open('webscraping/pokedex_missingTypes.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            insert_pokemon(row)


def types():
    with open('webscraping/types.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            insert_types(row)


def moves():
    with open('webscraping/moves.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=':')
        next(csv_reader)
        for row in csv_reader:
            insert_moves(row)


def movesCat():
    with open('webscraping/movesCategory.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            insert_movesCat(row)


if __name__ == '__main__':

    # main function adds pokedex_missingTypes.csv to pokemon table
    # main()
    # types function adds types.csv to pokemon table
    # types()
    # moves function adds moves.csv to moves table
    # moves()
    # movesCat function adds movesCategory.csv to moves table (updates category attr)
    movesCat()
