import os
from flask import Flask, render_template, request, flash
from flask_login import LoginManager
from .extensions import db
from .views import bp as core
from .models import User

from config import Config

login = LoginManager()
login.login_view = 'core.login'

def create_app(myConfig=Config):
    """
    Pokedex application factory
    """
    app = Flask(__name__)
    app.config.from_object(myConfig)
    
    app.register_blueprint(core)

    login.init_app(app)
    @login.user_loader
    def load_user(id):
        return User.query.get(id)
    extensions(app)
    
        
    return app

def extensions(app):
    db.init_app(app)
    return None


def authentication(app, user_model):
    login_manager.login_view = 'login'
        
    # @login.user_loader
    # def load_user(id):
    #     return User.query.get(int(id))
    pass



# # homepage
# @app.route('/', methods=['GET','POST'])
# def index():
#     if request.method == 'POST':
#         pokemon = request.form['pokemon']
#         flash(pokemon)
#     return render_template('index.html', title='Home')


