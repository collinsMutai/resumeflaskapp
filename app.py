import os, sys
from flask import Flask, request, abort, jsonify, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, TextAreaField, HiddenField, SelectField
from flask_wtf.file import FileField, FileAllowed




from models import setup_db, Userinput





# App Config.
def create_app(test_config=None):
  # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    db = SQLAlchemy(app)
    # migrate = Migrate(app, db)



    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
        return response


    class Contact(FlaskForm):
        name = StringField('Name')
        phone = StringField('Phone')
        message = StringField('message')
   

    @app.route('/', methods=['GET', 'POST'])
    def index():

        form = Contact(request.form)

        if form.validate_on_submit():
   
            name = form.name.data
            phone = form.phone.data
            message = form.message.data

            newMessage = Userinput(
                name=name,
                phone=phone,
                message=message,
            )
            db.session.add(newMessage)

            db.session.commit()




        return render_template('index.html', form=form)








    return app


app = create_app()

if __name__ == '__main__':
    manager.run()















    # export FLASK_APP=app.py FLASK_DEBUG=true
    # flask run


    #  python manage.py db init
    #  python manage.py db migrate
    #  python manage.py db upgrade

    # heroku login
    # heroku create flaskresumeapp

    # heroku addons:create heroku-postgresql:hobby-dev --app flaskresumeapp

    # heroku config --app flaskresumeapp


    # DATABASE_URL: postgres://rkfnxmnomtqvnc:a08200494aaed517993a50024f3780f361e2c35e4cb163e8590e2476e1d93ab0@ec2-52-86-2-228.compute-1.amazonaws.com:5432/df4gkmgu7317r9

    # deploy
    # git init
    # heroku git:remote -a flaskresumeapp
    # git add .
    # git commit -m ""
    # git push heroku master
