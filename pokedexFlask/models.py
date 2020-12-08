from pokedexFlask.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



# from sqlalchemy.ext.automap import automap_base
# Base = automap_base()
# Base.prepare(db.engine, reflect=True)
# Moves = Base.classes.moves
# PokemonTypes = Base.classes.pokemontypes
# Pokemon = Base.classes.pokemon
# PokemonMoveSets = Base.classes.pokemonmovesets

class Moves(db.Model):
    __tablename__   = "moves"
    __table_args__  = {'extend_existing': True}
    
    name     = db.Column(db.String(30), primary_key=True, nullable=False)
    type = db.Column(db.String(10), nullable=False)
    category = db.Column(db.String(10))
    pp       = db.Column(db.Integer, nullable=False)
    power    = db.Column(db.Integer)
    accuracy = db.Column(db.Integer)
    description = db.Column(db.String(200), nullable=False)
    

class PokemonMoveSets(db.Model):
    __tablename__ = 'pokemonmovesets'
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.Integer, primary_key=True)
    
    pokeID  = db.Column(db.Integer)
    moveName = db.Column(db.String(30))


class Pokemon(db.Model):
    __tablename__ = "pokemon"
    __table_args__ = {'extend_existing': True}
    
    pokeID  = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(20), nullable=False)
    primaryType     = db.Column(db.String(), nullable=False)
    secondaryType   = db.Column(db.String(20))
    ability1 = db.Column(db.String(20))
    ability2 = db.Column(db.String(20))
    ability3 = db.Column(db.String(20))
    hp      = db.Column(db.Integer, nullable=False)
    attack  = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    sp_attack  = db.Column(db.Integer, nullable=False)
    sp_defense = db.Column(db.Integer, nullable=False)
    speed  = db.Column(db.Integer, nullable=False)
    region = db.Column(db.String(20), nullable=False)



class PokemonTypes(db.Model):
        __tablename__ = "pokemontypes"
        __table_args__ = {'extend_existing': True} 
        
        name = db.Column(db.String(10), primary_key=True, nullable=False)
        normal   = db.Column(db.Float)
        fire     = db.Column(db.Float)
        water    = db.Column(db.Float)
        electric = db.Column(db.Float)
        grass    = db.Column(db.Float)
        ice      = db.Column(db.Float)
        fighting = db.Column(db.Float)
        poison   = db.Column(db.Float)
        ground   = db.Column(db.Float)
        flying   = db.Column(db.Float)
        psychic  = db.Column(db.Float)
        bug      = db.Column(db.Float)
        rock     = db.Column(db.Float)
        ghost    = db.Column(db.Float)
        dragon   = db.Column(db.Float)
        dark     = db.Column(db.Float)
        steel    = db.Column(db.Float)
        fairy    = db.Column(db.Float)
        ID       = db.Column(db.Integer, nullable=False)



    

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    
    # Authentication
    username  = db.Column(db.String(24), unique=True, index=True)
    email     = db.Column(db.String(255), unique=True, index=True, nullable=False, server_default='')
    password  = db.Column(db.String(128), nullable=False, server_default='1')

    
    def __init__(self, **kwargs):
        # Call Flask-SQLAlchemy's constructor.
        super(User, self).__init__(**kwargs)
    

    @classmethod
    def find_by_identity(cls, identity):
        """ Find user by username"""
        return User.query.filter((User.username == identity)).first()

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    

    # @login.user_loader
    # def load_user(id):
    # return User.query.get(int(id))



class Team(db.Model):

    __tablename__ = "team"
    __table_args__ = {'extend_existing': True} 
    # userID  = db.Column(db.Integer, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), nullable=False)


    pokemonName = db.Column(db.String(20))  # pokemon 1's name
    # pokemon2 = db.Column(db.String(20))
    # pokemon3 = db.Column(db.String(20))
    # pokemon4 = db.Column(db.String(20))
    # pokemon5 = db.Column(db.String(20))
    # pokemon6 = db.Column(db.String(20))
    # pokemon_ID    = db.Column(db.Integer)     # pokemon 1's ID 
    # pokemon_ptype = db.Column(db.String(10))  # pokemon 1's primary type
    # pokemon_type  = db.Column(db.String(10))  # pokemon 1's secondary type
    
    # @classmethod
    # def has_team(self, userID):
    #     if userID 
    #     pass