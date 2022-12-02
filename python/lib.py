from flask import Flask, render_template, request, redirect, session, url_for, flash, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from datetime import datetime
from werkzeug.utils import secure_filename
import os
import base64
import uuid


template_dir = os.path.abspath('./')#change template folder location for render_remplate
static_dir = os.path.abspath('./static')#change default css and js folder
profilePicturePath = "/Users/User/Documents/pro/Bug Tracker/static/profilePictures"
allowedExtensions = {'png', 'jpg', 'jpeg'}


app = Flask(__name__, template_folder=template_dir,static_folder=static_dir)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database/test.db' #three / is relative path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = profilePicturePath

db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login.loginPage"
login_manager.login_message = "You need to be logged in to access this page"
login_manager.login_message_category = "warning"
app.secret_key = b"377252112254372214101015264317"

app.jinja_env.globals.update(len=len)
app.jinja_env.globals.update(str=str)

@app.after_request  #asks the browser not to cache the prev page so user cannot access login_required pages after logged out by using back button
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response


@login_manager.user_loader
def load_user(id):
    return Accounts.query.get(int(id))

class LoginForm(FlaskForm):
    email=EmailField('Email')
    password=PasswordField('Password')

ProjectUserRelationship = db.Table('project_user_relationship',
    db.Column('user_id', db.Integer, db.ForeignKey('accounts.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('projects.id'))
)

TaskUserRelationship = db.Table('task_user_relationship', 
db.Column('user_id', db.Integer, db.ForeignKey('accounts.id')), 
db.Column('task_id', db.Integer, db.ForeignKey('tasks.id'))
)


class Accounts(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    bio = db.Column(db.String(1000), nullable=False)
    profile_picture_metadata = db.Column(db.String(1000), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    onProject = db.relationship('Projects', secondary=ProjectUserRelationship, backref="members")
    owns = db.relationship('Projects', backref='owner')
    workingOn = db.relationship('Tasks', secondary=TaskUserRelationship ,backref='workedOnBy')

    def __repr__(self):
        return '<Account %r>' % self.username

class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(70))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    owner_id = db.Column(db.Integer, db.ForeignKey('accounts.id'))
    tasks = db.relationship('Tasks', backref="project")
    url = db.Column(db.String(70))

    def __repr__(self):
        return '<Project %r>' % self.name




class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True) #???
    name = db.Column(db.String(70))
    description = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    state = db.Column(db.Boolean) # unfinished / finished


    def __repr__(self):
        return '<Tasks %r>' % self.name



def allowedFileExtensions(filename):
    if filename.split('.')[1] in allowedExtensions:
        return True
    return False
