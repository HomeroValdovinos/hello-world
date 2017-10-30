from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/cinta_roja_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Login(db.Model):
    id_user = db.Column(db.Integer, primary_key=True, unique=True)
    user_name = db.Column(db.String(32), unique=True, nullable=False)
    user_password = db.Column(db.String(32), unique=False, nullable=False)

    # def __repr__(self):
    #     return '<User %r>' % self.username


db.create_all()

