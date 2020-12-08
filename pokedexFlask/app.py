from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://[user]:[pass]@[host]/[db]'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

# NOTHING BELOW THIS LINE NEEDS TO CHANGE
# this route will test the database connection and nothing more
@app.route('/')
def testdb():
    try:
        db.session.query('1').from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

if __name__ == '__main__':
    app.run(debug=True)

# # homepage
# @app.route('/', methods=['GET','POST'])
# def index():
#     if request.method == 'POST':
#         pokemon = request.form['pokemon']
#         flash(pokemon)
#     return render_template('index.html', title='Home')




if __name__ == '__main__':
    app.run(debug=True)