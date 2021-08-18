import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json


database_name = "resumeapp"
database_path = "postgresql://{}:{}@{}/{}".format('postgres', '7749','localhost:5432', database_name)

# database_path = os.environ['DATABASE_URL']
database_path = os.getenv('DATABASE_URL', database_path)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SECRET_KEY'] = 'mysecret'
    db.app = app
    db.init_app(app)
    db.drop_all()
    db.create_all()


class Userinput(db.Model):
    __tablename__ = "userinputs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone = db.Column(db.String)
    message = db.Column(db.String)



    def __init__(self, name, phone, message):
        self.name = name
        self.phone = phone
        self.message = message


    def insert(self):
        db.session.add(self)
        db.session.commit()


    def update(self):
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "message": self.message,
        }