from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, Length, EqualTo
from .models import User

class SearchPokemon(FlaskForm):
    pokemonName   = SelectField('Pokemon Name', validators=[DataRequired()])
    submit        = SubmitField('Search')

class SearchFiltersForm(FlaskForm):
    pokePrimType  = SelectField('Primary Type', choices= [('none', 'select type'), ('normal','normal'), ('fire','fire'), ('water','water'), ('electric','electric'), ('grass','grass'), ('ice', 'ice'), ('fighting', 'fighting'), ('poison', 'poison'), ('ground', 'ground'), ('flying', 'flying'), ('psychic', 'psychic'), ('bug', 'bug'), ('rock', 'rock'), ('ghost', 'ghost'), ('dragon', 'dragon'), ('dark', 'dark'), ('steel', 'steel'), ('fairy', 'fairy')])
    pokeSecType   = SelectField('Secondary Type', choices= [('none', 'select type'), ('normal','normal'), ('fire','fire'), ('water','water'), ('electric','electric'), ('grass','grass'), ('ice', 'ice'), ('fighting', 'fighting'), ('poison', 'poison'), ('ground', 'ground'), ('flying', 'flying'), ('psychic', 'psychic'), ('bug', 'bug'), ('rock', 'rock'), ('ghost', 'ghost'), ('dragon', 'dragon'), ('dark', 'dark'), ('steel', 'steel'), ('fairy', 'fairy')])
    pokeAtk       = SelectField('Attack Stat', choices=[('none', 'select range'), ('<25', '<25'), ('25-50', '25-50'), ('51-75','51-75'), ('76-100','76-100'), ('>100','>100')])
    pokeDef       = SelectField('Defense Stat', choices=[('none', 'select range'), ('<25', '<25'), ('25-50', '25-50'), ('51-75', '51-75'), ('76-100', '76-100'), ('>100', '>100')])
    pokeSpd       = SelectField('Speed Stat', choices=[('none','select range'), ('<25','<25'), ('25-50','25-50'), ('51-75','51-75'), ('76-100','76-100'), ('>100','>100')])
    pokeSpAtk     = SelectField('Special Attack Stat', choices= [('none', 'select range'), ('<25', '<25'), ('25-50', '25-50'), ('51-75', '51-75'), ('76-100', '76-100'), ('>100', '>100')])
    pokeSpDef     = SelectField('Special Defense Stat', choices= [('none','select range'), ('<25','<25'), ('25-50','25-50'), ('51-75', '51-75'), ('76-100','76-100'), ('>100', '>100')])
    pokeHP        = SelectField('Health Points Stat', choices= [('none', 'select range'), ('<25', '<25'), ('25-50', '25-50'), ('51-75', '51-75'), ('76-100', '76-100'), ('>100', '>100')])
   # pokeTotal = SelectField('Stat Total', choices = [('none', 'select range'), ('<150', '<150'), ('151-300', '156-300'), ('301-450', '301-450'), ('451-650', '451-600'), ('>600', '>600')])
    submit        = SubmitField('Search')

class MovesForm(FlaskForm):
    pokemon = SelectField("Look up a pokemon's moveset", validators=[DataRequired()])
    submit  = SubmitField('Search')
    
class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired(), Length(8, 128)])
    submit   = SubmitField('LogIn')
    
    def ValidateUsername(self, username):
        user = User.find_by_identity(username=username.data)
        if user is not None:
            raise ValidationError('Username not found')

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField(validators= [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired(), Length(8, 128)])
    password2 = PasswordField('Confirm password', [DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Register')

    def ValidateUsername(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username')
    
    def ValidateEmail(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address')

class TeamForm(FlaskForm):
    # pokemon1 = StringField('Pokemon #1')
    pokemon1 = SelectField('Pokemon #1', validators=[DataRequired()])
    pokemon2 = SelectField('Pokemon #2', validators=[DataRequired()])
    pokemon3 = SelectField('Pokemon #3', validators=[DataRequired()])
    pokemon4 = SelectField('Pokemon #4', validators=[DataRequired()])
    pokemon5 = SelectField('Pokemon #5', validators=[DataRequired()])
    pokemon6 = SelectField('Pokemon #6', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class MyTeamForm(FlaskForm):
    strongAgainst = SelectField('Pokemon Weak Against', validators=[DataRequired()])
    submit = SubmitField('Search')