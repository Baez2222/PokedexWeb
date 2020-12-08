from flask import Blueprint, render_template,request, redirect, url_for, flash

from sqlalchemy.orm import sessionmaker, scoped_session
import sqlalchemy
from .extensions import db

from pokedexFlask.models import User, Pokemon, Team
from .forms import LoginForm, SignupForm, SearchFiltersForm, TeamForm, MovesForm, SearchPokemon, MyTeamForm

from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse



bp = Blueprint('core', __name__, template_folder='templates')

engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3307/pokedex')
Session = scoped_session(sessionmaker(bind=engine))
s = Session()

@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    nameForm = SearchPokemon()
    form = SearchFiltersForm()
    pokemonName=''
    pokePrimType=''
    pokeSecType=''
    pokeBothType=''
    pokeNoType=''
    pokeAtk=''
    pokeDef=''
    pokeSpd=''
    pokeSpAtk=''
    pokeSpDef=''
    pokeHP=''

    # gets pokemon names for dropdown menu
    available_name = Pokemon.query.order_by(Pokemon.name).all()
    name_list = [(i.name) for i in available_name]
    nameForm.pokemonName.choices = ['select name'] + name_list
    
    if nameForm.pokemonName.data !='none':
            q0=nameForm.pokemonName.data
            pokemonName = s.execute('SELECT * FROM pokemon p \
                WHERE p.name = :v0', {'v0': q0})

    if form.validate_on_submit():
        
    # ----- Different Queries Based on Type and Stat Filters
        # --- Searching by just Primary Type
        if form.pokePrimType.data != 'none' and form.pokeSecType.data == 'none':
            q1 = form.pokePrimType.data
            q3 = -1
            q4 = 999
            q5 = -1
            q6 = 999
            q7 = -1
            q8 = 999
            q9 = -1
            q10 = 999
            q11 = -1
            q12 = 999
            q13 = -1
            q14 = 999
            
            # Atk filter
            if(form.pokeAtk.data == '<25'):
                q3 = 0
                q4 = 24
            elif(form.pokeAtk.data == '25-50'):
                q3 = 25
                q4 = 50
            elif(form.pokeAtk.data == '51-75'):
                q3 = 51
                q4 = 75
            elif(form.pokeAtk.data == '76-100'):
                q3 = 76
                q4 = 100
            elif(form.pokeAtk.data == '>100'):
                q3 = 101
                q4 = 999
            
            # Def filter
            if(form.pokeDef.data == '<25'):
                q5 = -1
                q6 = 24
            elif(form.pokeDef.data == '25-50'):
                q5 = 25
                q6 = 50
            elif(form.pokeDef.data == '51-75'):
                q5 = 51
                q6 = 75
            elif(form.pokeDef.data == '76-100'):
                q5 = 76
                q6 = 100
            elif(form.pokeDef.data == '>100'):
                q5 = 101
                q6 = 999

             # Spd filter
            if(form.pokeSpd.data == '<25'):
                q7 = -1
                q8 = 24
            elif(form.pokeSpd.data == '25-50'):
                q7 = 25
                q8 = 50
            elif(form.pokeSpd.data == '51-75'):
                q7 = 51
                q8 = 75
            elif(form.pokeSpd.data == '76-100'):
                q7 = 76
                q8 = 100
            elif(form.pokeSpd.data == '>100'):
                q7 = 101
                q8 = 999
                    
            # SpAtk filter
            if(form.pokeSpAtk.data == '<25'):
                q9 = -1
                q10 = 24
            elif(form.pokeSpAtk.data == '25-50'):
                q9 = 25
                q10 = 50
            elif(form.pokeSpAtk.data == '51-75'):
                q9 = 51
                q10 = 75
            elif(form.pokeSpAtk.data == '76-100'):
                q9 = 76
                q10 = 100
            elif(form.pokeSpAtk.data == '>100'):
                q9 = 101
                q10 = 999

            # SpDef filter
            if(form.pokeSpDef.data == '<25'):
                q11 = -1
                q12 = 24
            elif(form.pokeSpDef.data == '25-50'):
                q11 = 25
                q12 = 50
            elif(form.pokeSpDef.data == '51-75'):
                q11 = 51
                q12 = 75
            elif(form.pokeSpDef.data == '76-100'):
                q11 = 76
                q12 = 100
            elif(form.pokeSpDef.data == '>100'):
                q11 = 101
                q12 = 999

            # HP filter
            if(form.pokeHP.data == '<25'):
                q13 = -1
                q14 = 24
            elif(form.pokeHP.data == '25-50'):
                q13 = 25
                q14 = 50
            elif(form.pokeHP.data == '51-75'):
                q13 = 51
                q14 = 75
            elif(form.pokeHP.data == '76-100'):
                q13 = 76
                q14 = 100
            elif(form.pokeHP.data == '>100'):
                q13 = 101
                q14 = 999
                
            pokePrimType = s.execute('SELECT * FROM pokemon p \
                WHERE p.primaryType = :v1 \
                AND p.attack >= :v3 AND p.attack <= :v4 \
                AND p.defense >= :v5 AND p.defense <= :v6 \
                AND p.speed >= :v7 AND p.speed <= :v8 \
                AND p.sp_attack >= :v9 AND p.sp_attack <= :v10 \
                AND p.sp_defense >= :v11 AND p.sp_defense <= :v12 \
                AND p.hp >= :v13 AND p.hp <= :v14', 
                {'v1': q1, 'v3':q3, 'v4': q4, 'v5':q5, 'v6': q6, 'v7' : q7, 'v8':q8, 'v8':q8, 'v9':q9, 'v10':q10, 'v11':q11, 'v12':q12, 'v13':q13, 'v14':q14})

        # --- Searching by just Secondary Type
        elif form.pokePrimType.data == 'none' and form.pokeSecType.data != 'none':
            q2 = form.pokeSecType.data
            q3 = -1
            q4 = 999
            q5 = -1
            q6 = 999
            q7 = -1
            q8 = 999
            q9 = -1
            q10 = 999
            q11 = -1
            q12 = 999
            q13 = -1
            q14 = 999

            # Atk filter
            if(form.pokeAtk.data == '<25'):
                q3 = 0
                q4 = 24
            elif(form.pokeAtk.data == '25-50'):
                q3 = 25
                q4 = 50
            elif(form.pokeAtk.data == '51-75'):
                q3 = 51
                q4 = 75
            elif(form.pokeAtk.data == '76-100'):
                q3 = 76
                q4 = 100
            elif(form.pokeAtk.data == '>100'):
                q3 = 101
                q4 = 999
            
            # Def filter
            if(form.pokeDef.data == '<25'):
                q5 = -1
                q6 = 24
            elif(form.pokeDef.data == '25-50'):
                q5 = 25
                q6 = 50
            elif(form.pokeDef.data == '51-75'):
                q5 = 51
                q6 = 75
            elif(form.pokeDef.data == '76-100'):
                q5 = 76
                q6 = 100
            elif(form.pokeDef.data == '>100'):
                q5 = 101
                q6 = 999

             # Spd filter
            if(form.pokeSpd.data == '<25'):
                q7 = -1
                q8 = 24
            elif(form.pokeSpd.data == '25-50'):
                q7 = 25
                q8 = 50
            elif(form.pokeSpd.data == '51-75'):
                q7 = 51
                q8 = 75
            elif(form.pokeSpd.data == '76-100'):
                q7 = 76
                q8 = 100
            elif(form.pokeSpd.data == '>100'):
                q7 = 101
                q8 = 999
            
            # SpAtk filter
            if(form.pokeSpAtk.data == '<25'):
                q9 = -1
                q10 = 24
            elif(form.pokeSpAtk.data == '25-50'):
                q9 = 25
                q10 = 50
            elif(form.pokeSpAtk.data == '51-75'):
                q9 = 51
                q10 = 75
            elif(form.pokeSpAtk.data == '76-100'):
                q9 = 76
                q10 = 100
            elif(form.pokeSpAtk.data == '>100'):
                q9 = 101
                q10 = 999

            # SpDef filter
            if(form.pokeSpDef.data == '<25'):
                q11 = -1
                q12 = 24
            elif(form.pokeSpDef.data == '25-50'):
                q11 = 25
                q12 = 50
            elif(form.pokeSpDef.data == '51-75'):
                q11 = 51
                q12 = 75
            elif(form.pokeSpDef.data == '76-100'):
                q11 = 76
                q12 = 100
            elif(form.pokeSpDef.data == '>100'):
                q11 = 101
                q12 = 999

            # HP filter
            if(form.pokeHP.data == '<25'):
                q13 = -1
                q14 = 24
            elif(form.pokeHP.data == '25-50'):
                q13 = 25
                q14 = 50
            elif(form.pokeHP.data == '51-75'):
                q13 = 51
                q14 = 75
            elif(form.pokeHP.data == '76-100'):
                q13 = 76
                q14 = 100
            elif(form.pokeHP.data == '>100'):
                q13 = 101
                q14 = 999
                

            pokeSecType = s.execute('SELECT * FROM pokemon p \
                WHERE p.secondaryType = :v2 \
                AND p.attack >= :v3 AND p.attack <= :v4 \
                AND p.defense >= :v5 AND p.defense <= :v6 \
                AND p.speed >= :v7 AND p.speed <= :v8 \
                AND p.sp_attack >= :v9 AND p.sp_attack <= :v10 \
                AND p.sp_defense >= :v11 AND p.sp_defense <= :v12 \
                AND p.hp >= :v13 AND p.hp <= :v14', 
                {'v2':q2, 'v3':q3, 'v4':q4, 'v5': q5, 'v6':q6, 'v7':q7, 'v8':q8, 'v8':q8, 'v9':q9, 'v10':q10, 'v11':q11, 'v12':q12, 'v13':q13, 'v14':q14})

        # --- Searching by both Primary and Secondary Types                
        elif form.pokePrimType.data != 'none' and form.pokeSecType.data != 'none':
            q1 = form.pokePrimType.data
            q2 = form.pokeSecType.data
            q3 = -1
            q4 = 999
            q5 = -1
            q6 = 999
            q7 = -1
            q8 = 999
            q9 = -1
            q10 = 999
            q11 = -1
            q12 = 999
            q13 = -1
            q14 = 999

            # --- Atk filter
            if(form.pokeAtk.data == '<25'):
                q3 = 0
                q4 = 24
            elif(form.pokeAtk.data == '25-50'):
                q3 = 25
                q4 = 50
            elif(form.pokeAtk.data == '51-75'):
                q3 = 51
                q4 = 75
            elif(form.pokeAtk.data == '76-100'):
                q3 = 76
                q4 = 100
            elif(form.pokeAtk.data == '>100'):
                q3 = 101
                q4 = 999
                
             # --- Def filter
            if(form.pokeDef.data == '<25'):
                q5 = -1
                q6 = 24
            elif(form.pokeDef.data == '25-50'):
                q5 = 25
                q6 = 50
            elif(form.pokeDef.data == '51-75'):
                q5 = 51
                q6 = 75
            elif(form.pokeDef.data == '76-100'):
                q5 = 76
                q6 = 100
            elif(form.pokeDef.data == '>100'):
                q5 = 101
                q6 = 999

            # Spd filter
            if(form.pokeSpd.data == '<25'):
                q7 = -1
                q8 = 24
            elif(form.pokeSpd.data == '25-50'):
                q7 = 25
                q8 = 50
            elif(form.pokeSpd.data == '51-75'):
                q7 = 51
                q8 = 75
            elif(form.pokeSpd.data == '76-100'):
                q7 = 76
                q8 = 100
            elif(form.pokeSpd.data == '>100'):
                q7 = 101
                q8 = 999
                
            # SpAtk filter
            if(form.pokeSpAtk.data == '<25'):
                q9 = -1
                q10 = 24
            elif(form.pokeSpAtk.data == '25-50'):
                q9 = 25
                q10 = 50
            elif(form.pokeSpAtk.data == '51-75'):
                q9 = 51
                q10 = 75
            elif(form.pokeSpAtk.data == '76-100'):
                q9 = 76
                q10 = 100
            elif(form.pokeSpAtk.data == '>100'):
                q9 = 101
                q10 = 999

            # SpDef filter
            if(form.pokeSpDef.data == '<25'):
                q11 = -1
                q12 = 24
            elif(form.pokeSpDef.data == '25-50'):
                q11 = 25
                q12 = 50
            elif(form.pokeSpDef.data == '51-75'):
                q11 = 51
                q12 = 75
            elif(form.pokeSpDef.data == '76-100'):
                q11 = 76
                q12 = 100
            elif(form.pokeSpDef.data == '>100'):
                q11 = 101
                q12 = 999
                
            # HP filter
            if(form.pokeHP.data == '<25'):
                q13 = -1
                q14 = 24
            elif(form.pokeHP.data == '25-50'):
                q13 = 25
                q14 = 50
            elif(form.pokeHP.data == '51-75'):
                q13 = 51
                q14 = 75
            elif(form.pokeHP.data == '76-100'):
                q13 = 76
                q14 = 100
            elif(form.pokeHP.data == '>100'):
                q13 = 101
                q14 = 999
                
            
            pokeBothType = s.execute('SELECT * FROM pokemon p \
                WHERE p.primaryType = :v1 AND p.secondaryType = :v2 \
                AND p.attack >= :v3 AND p.attack <= :v4 \
                AND p.defense >= :v5 AND p.defense <= :v6 \
                AND p.speed >= :v7 AND p.speed <= :v8 \
                AND p.sp_attack >= :v9 AND p.sp_attack <= :v10 \
                AND p.sp_defense >= :v11 AND p.sp_defense <= :v12 \
                AND p.hp >= :v13 AND p.hp <= :v14', 
                {'v1':q1,'v2':q2, 'v3':q3, 'v4':q4, 'v5': q5, 'v6': q6, 'v7':q7, 'v8':q8, 'v8':q8, 'v9':q9, 'v10':q10, 'v11':q11, 'v12':q12, 'v13':q13, 'v14':q14})

        # --- Searching by just Stats        
        elif form.pokePrimType.data == 'none' and form.pokeSecType.data == 'none':
            q3 = -1
            q4 = 999
            q5 = -1
            q6 = 999
            q7 = -1
            q8 = 999
            q9 = -1
            q10 = 999
            q11 = -1
            q12 = 999
            q13 = -1
            q14 = 999


            # --- Atk filter
            if(form.pokeAtk.data == '<25'):
                q3 = 0
                q4 = 24
            elif(form.pokeAtk.data == '25-50'):
                q3 = 25
                q4 = 50
            elif(form.pokeAtk.data == '51-75'):
                q3 = 51
                q4 = 75
            elif(form.pokeAtk.data == '76-100'):
                q3 = 76
                q4 = 100
            elif(form.pokeAtk.data == '>100'):
                q3 = 101
                q4 = 999

            # --- Def filter
            if(form.pokeDef.data == '<25'):
                q5 = -1
                q6 = 24
            elif(form.pokeDef.data == '25-50'):
                q5 = 25
                q6 = 50
            elif(form.pokeDef.data == '51-75'):
                q5 = 51
                q6 = 75
            elif(form.pokeDef.data == '76-100'):
                q5 = 76
                q6 = 100
            elif(form.pokeDef.data == '>100'):
                q5 = 101
                q6 = 999

            # Spd filter
            if(form.pokeSpd.data == '<25'):
                q7 = -1
                q8 = 24
            elif(form.pokeSpd.data == '25-50'):
                q7 = 25
                q8 = 50
            elif(form.pokeSpd.data == '51-75'):
                q7 = 51
                q8 = 75
            elif(form.pokeSpd.data == '76-100'):
                q7 = 76
                q8 = 100
            elif(form.pokeSpd.data == '>100'):
                q7 = 101
                q8 = 999

            # SpAtk filter
            if(form.pokeSpAtk.data == '<25'):
                q9 = -1
                q10 = 24
            elif(form.pokeSpAtk.data == '25-50'):
                q9 = 25
                q10 = 50
            elif(form.pokeSpAtk.data == '51-75'):
                q9 = 51
                q10 = 75
            elif(form.pokeSpAtk.data == '76-100'):
                q9 = 76
                q10 = 100
            elif(form.pokeSpAtk.data == '>100'):
                q9 = 101
                q10 = 999
            
            # SpDef filter
            if(form.pokeSpDef.data == '<25'):
                q11 = -1
                q12 = 24
            elif(form.pokeSpDef.data == '25-50'):
                q11 = 25
                q12 = 50
            elif(form.pokeSpDef.data == '51-75'):
                q11 = 51
                q12 = 75
            elif(form.pokeSpDef.data == '76-100'):
                q11 = 76
                q12 = 100
            elif(form.pokeSpDef.data == '>100'):
                q11 = 101
                q12 = 999

            # HP filter
            if(form.pokeHP.data == '<25'):
                q13 = -1
                q14 = 24
            elif(form.pokeHP.data == '25-50'):
                q13 = 25
                q14 = 50
            elif(form.pokeHP.data == '51-75'):
                q13 = 51
                q14 = 75
            elif(form.pokeHP.data == '76-100'):
                q13 = 76
                q14 = 100
            elif(form.pokeHP.data == '>100'):
                q13 = 101
                q14 = 999
            

            pokeNoType = s.execute('SELECT * FROM pokemon p \
                WHERE  p.attack >= :v3 AND p.attack <= :v4 \
                AND p.defense >= :v5 AND p.defense <= :v6 \
                AND p.speed >= :v7 AND p.speed <= :v8 \
                AND p.sp_attack >= :v9 AND p.sp_attack <= :v10 \
                AND p.sp_defense >= :v11 AND p.sp_defense <= :v12 \
                AND p.hp >= :v13 AND p.hp <= :v14',
                {'v3':q3, 'v4':q4, 'v5':q5, 'v6':q6, 'v7':q7, 'v8':q8, 'v9':q9, 'v10':q10, 'v11':q11, 'v12':q12, 'v13':q13, 'v14':q14 })
            
    return render_template('index.html', Title='home',nameForm=nameForm, form=form, pokemonName=pokemonName, pokePrimType=pokePrimType, pokeSecType=pokeSecType, pokeBothType=pokeBothType, pokeNoType=pokeNoType)


@bp.route('/moves', methods=['GET', 'POST'])
@login_required
def moves():
    form = MovesForm()
    available_name = Pokemon.query.order_by(Pokemon.name).all()
    name_list = [(i.name) for i in available_name]
    form.pokemon.choices = name_list
    pokemon=''
    if form.validate_on_submit():
        pokemon = form.pokemon.data
        pokemon = s.execute('SELECT ms.*, p.name, m.* FROM pokemonmovesets ms JOIN pokemon p ON p.pokeID = ms.pokeID \
            JOIN moves m ON m.name = ms.moveName WHERE p.name = :v0', {'v0': form.pokemon.data})
    return render_template('moves.html', title='Moves', form=form, pokemon=pokemon)

@bp.route('/createteam', methods=['GET', 'POST'])
@login_required
def createteam():
    form=TeamForm()
    # available_name=db.session.query.(Pokemon).all()
    available_name = Pokemon.query.order_by(Pokemon.name).all()
    name_list = [(i.name) for i in available_name]
    form.pokemon1.choices = name_list
    form.pokemon2.choices = name_list
    form.pokemon3.choices = name_list
    form.pokemon4.choices = name_list
    form.pokemon5.choices = name_list
    form.pokemon6.choices = name_list
    if form.validate_on_submit():
        # t = Team(username=current_user.username,
        #          pokemon1=form.pokemon1.data,
        #          pokemon2=form.pokemon2.data,
        #          pokemon3=form.pokemon3.data,
        #          pokemon4=form.pokemon4.data,
        #          pokemon5=form.pokemon5.data,
        #          pokemon6=form.pokemon6.data)
        existing_team = Team.query.filter_by(username=current_user.username).first()
        if existing_team is None:
            db.session.add(Team(username=current_user.username, pokemonName=form.pokemon1.data))
            db.session.add(Team(username=current_user.username, pokemonName=form.pokemon2.data))
            db.session.add(Team(username=current_user.username, pokemonName=form.pokemon3.data))
            db.session.add(Team(username=current_user.username, pokemonName=form.pokemon4.data))
            db.session.add(Team(username=current_user.username, pokemonName=form.pokemon5.data))
            db.session.add(Team(username=current_user.username, pokemonName=form.pokemon6.data))
            db.session.commit()
            return redirect(url_for('.createteam'))
        else:
            s.execute(Team.__table__.delete().where(Team.username==current_user.username))
            s.commit()
            db.session.add(Team(username=current_user.username, pokemonName=form.pokemon1.data))
            db.session.add(Team(username=current_user.username, pokemonName=form.pokemon2.data))
            db.session.add(Team(username=current_user.username, pokemonName=form.pokemon3.data))
            db.session.add(Team(username=current_user.username, pokemonName=form.pokemon4.data))
            db.session.add(Team(username=current_user.username, pokemonName=form.pokemon5.data))
            db.session.add(Team(username=current_user.username, pokemonName=form.pokemon6.data))
            db.session.commit()
            
            return redirect(url_for('.createteam'))
    return render_template('createteam.html', title='Create Team', form=form)

@bp.route('/myteam', methods=['GET', 'POST'])
@login_required
def myteam():
    form = MyTeamForm()
    # gets your team base stats
    existing_team = s.execute('SELECT p.* FROM team t \
                JOIN pokemon p ON t.pokemonName = p.name WHERE t.username = :v0', {'v0': current_user.username})

    # getting values for dropdown menu
    available_name = s.execute('SELECT p.name FROM team t \
                 JOIN pokemon p ON t.pokemonName = p.name WHERE t.username = :v0', {'v0': current_user.username})
    name_list = [(i.name) for i in available_name]
    form.strongAgainst.choices = name_list

    strongAgainst=''
    effectiveAgainst=''
    
    # getting type coverage based on my team
    query=''
    poke1Coverage = { 'Normal':0,
                     'Fire':0,
                     'Water':0,
                     'Electric':0,
                     'Grass':0,
                     'Ice':0,
                     'Fighting':0,
                     'Poison':0,
                     'Ground':0,
                     'Flying':0,
                     'Psychic':0,
                     'Bug':0,
                     'Rock':0,
                     'Ghost':0,
                     'Dragon':0,
                     'Dark':0,
                     'Steel':0,
                     'Fairy':0}
    poke2Coverage = { 'Normal':0,
                     'Fire':0,
                     'Water':0,
                     'Electric':0,
                     'Grass':0,
                     'Ice':0,
                     'Fighting':0,
                     'Poison':0,
                     'Ground':0,
                     'Flying':0,
                     'Psychic':0,
                     'Bug':0,
                     'Rock':0,
                     'Ghost':0,
                     'Dragon':0,
                     'Dark':0,
                     'Steel':0,
                     'Fairy':0}
    poke3Coverage = { 'Normal':0,
                     'Fire':0,
                     'Water':0,
                     'Electric':0,
                     'Grass':0,
                     'Ice':0,
                     'Fighting':0,
                     'Poison':0,
                     'Ground':0,
                     'Flying':0,
                     'Psychic':0,
                     'Bug':0,
                     'Rock':0,
                     'Ghost':0,
                     'Dragon':0,
                     'Dark':0,
                     'Steel':0,
                     'Fairy':0}
    poke4Coverage = { 'Normal':0,
                     'Fire':0,
                     'Water':0,
                     'Electric':0,
                     'Grass':0,
                     'Ice':0,
                     'Fighting':0,
                     'Poison':0,
                     'Ground':0,
                     'Flying':0,
                     'Psychic':0,
                     'Bug':0,
                     'Rock':0,
                     'Ghost':0,
                     'Dragon':0,
                     'Dark':0,
                     'Steel':0,
                     'Fairy':0}
    poke5Coverage = { 'Normal':0,
                     'Fire':0,
                     'Water':0,
                     'Electric':0,
                     'Grass':0,
                     'Ice':0,
                     'Fighting':0,
                     'Poison':0,
                     'Ground':0,
                     'Flying':0,
                     'Psychic':0,
                     'Bug':0,
                     'Rock':0,
                     'Ghost':0,
                     'Dragon':0,
                     'Dark':0,
                     'Steel':0,
                     'Fairy':0}
    poke6Coverage = { 'Normal':0,
                     'Fire':0,
                     'Water':0,
                     'Electric':0,
                     'Grass':0,
                     'Ice':0,
                     'Fighting':0,
                     'Poison':0,
                     'Ground':0,
                     'Flying':0,
                     'Psychic':0,
                     'Bug':0,
                     'Rock':0,
                     'Ghost':0,
                     'Dragon':0,
                     'Dark':0,
                     'Steel':0,
                     'Fairy':0}
    pokeCoverageList = [poke1Coverage, poke2Coverage, poke3Coverage, poke4Coverage, poke5Coverage, poke6Coverage]
    counter=0
    for i in name_list:
        if query=='':
            query = 'SELECT name, COUNT(type) AS "occurrences", type FROM( \
                SELECT ms.moveName, p.name, m.type FROM pokemonmovesets ms JOIN pokemon p ON p.pokeID = ms.pokeID \
                JOIN moves m ON m.name = ms.moveName WHERE p.name = "%s" ) AS temp_table GROUP BY (type)' % (i)
        else:
            query += 'UNION SELECT name, COUNT(type) AS "occurrences", type FROM( \
                SELECT ms.moveName, p.name, m.type FROM pokemonmovesets ms JOIN pokemon p ON p.pokeID = ms.pokeID \
                JOIN moves m ON m.name = ms.moveName WHERE p.name = "%s" ) AS temp_table GROUP BY (type)' % (i)
        pokeCoverage = s.execute('SELECT COUNT(type) AS "occurrences", type FROM( \
                SELECT ms.moveName, p.name, m.type FROM pokemonmovesets ms JOIN pokemon p ON p.pokeID = ms.pokeID \
                JOIN moves m ON m.name = ms.moveName WHERE p.name = "%s" ) AS temp_table GROUP BY (type)' % (i))
        for row in pokeCoverage:
            pokeCoverageList[counter][row[1]] = int(row.occurrences)
        counter+=1
    coverageDict = { 'Normal':0,
                'Fire':0,
                'Water':0,
                'Electric':0,
                'Grass':0,
                'Ice':0,
                'Fighting':0,
                'Poison':0,
                'Ground':0,
                'Flying':0,
                'Psychic':0,
                'Bug':0,
                'Rock':0,
                'Ghost':0,
                'Dragon':0,
                'Dark':0,
                'Steel':0,
                'Fairy':0}
    if query != '':
        for key in coverageDict:
            coverageDict[key] = poke1Coverage[key] + poke2Coverage[key] + poke3Coverage[key] + poke4Coverage[key] + poke5Coverage[key] + poke6Coverage[key]
        for row in effectiveAgainst:
            coverageDict[row[1]] = int(row.occurrences)

    typeDict = { 1:'normal',
                 2:'fire',
                 3:'water',
                 4:'electric',
                 5:'grass',
                 6:'ice',
                 7:'fighting',
                 8:'poison',
                 9:'ground',
                 10:'flying',
                 11:'psychic',
                 12:'bug',
                 13:'rock',
                 14:'ghost',
                 15:'dragon',
                 16:'dark',
                 17:'steel',
                 18:'fairy'}
    if form.validate_on_submit():
        if form.strongAgainst.data != '':
            strongAgainst = s.execute('SELECT pt.* FROM pokemon p JOIN pokemonTypes pt ON pt.name = p.primaryType \
                WHERE p.name = :v0', {'v0': form.strongAgainst.data})
            typeList = []
            counter = 0
            for row in strongAgainst:
                for col in row:
                    if col == 2:
                        typeList.append(typeDict.get(counter))
                    counter += 1
            if len(typeList) == 0:
                return render_template('myteam.html', title='My Team', form=form, team=existing_team, strongAgainst=strongAgainst)

            query = ''
            for i in typeList:
                if query == '':
                    query = 'SELECT p.* FROM pokemon p WHERE p.primaryType = "%s"' % (i)
                else:
                    query += ' UNION SELECT p.* FROM pokemon p WHERE p.primaryType = "%s"' % (i)
            strongAgainst = s.execute(query)
            
    return render_template('myteam.html', title='My Team', form=form,  team=existing_team, strongAgainst=strongAgainst, \
        effectiveAgainst=coverageDict, poke1Coverage=poke1Coverage, poke2Coverage=poke2Coverage, poke3Coverage=poke3Coverage, \
            poke4Coverage=poke4Coverage, poke5Coverage=poke5Coverage, poke6Coverage=poke6Coverage)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('core.index'))
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter_by(username=form.username.data).first()
        if u and u.check_password(form.password.data):
            login_user(u)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('core.index')
            return redirect(next_page)
        else:
            return redirect(url_for('core.login'))
    return render_template('login.html', title='LogIn', form=form)

@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('core.login'))

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('core.index'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered!')
        return redirect(url_for('core.login'))
    return render_template('signup.html', title='Signup', form=form)

# NOTHING BELOW THIS LINE NEEDS TO CHANGE
# this route will test the database connection and nothing more
# @bp.route('/testdb')
# def testdb():
#     try:
#         db.session.query('1').from_statement(text('SELECT 1')).all()
#         return '<h1>It works.</h1>'
#     except Exception as e:
#         # e holds description of the error
#         error_text = "<p>The error:<br>" + str(e) + "</p>"
#         hed = '<h1>Something is broken.</h1>'
#         return hed + error_text