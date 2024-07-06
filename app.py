from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'markipliermilk'
db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(99), nullable = False)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/rating")
def rating():
    return render_template('rating.html')

@app.route('/stats')
def stats():
    return render_template('stats.html')

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug = True)