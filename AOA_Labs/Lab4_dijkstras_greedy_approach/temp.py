from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pass@localhost/adityaved'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class departments(db.Model):
    deptid = db.Column('deptid', db.Integer, primary_key=True)
    depname = db.Column(db.String(50))
    marks = db.Column(db.Integer)


