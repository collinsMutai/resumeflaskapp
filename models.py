import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
'''
setup_db(app):
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):    
    database_name ='resume_db'
    default_database_path= "postgres://{}:{}@{}/{}".format('postgres', '7749', 'localhost:5432', database_name)
    database_path = os.getenv('DATABASE_URL', default_database_path)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SECRET_KEY'] = 'mysecret' 
    # app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    db.app = app
    db.init_app(app)
    '''
    drops the database tables and starts fresh
    can be used to initialize a clean database
'''
def db_drop_and_create_all():
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