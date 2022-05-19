from tkinter import Y
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route("/", methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        Username = request.form.get('Username')
        Password = request.form.get('Password')
        
        user = User.query.filter_by(username=Username).first()
        if user:
            if user.password == Password:
                return redirect(url_for('views.login'))
            else:
                flash('The password is incorrect. Try it again.', category='error')
                return redirect(url_for('views.index'))
        else:
            flash('That is not a valid account. What about creating a new account?', category='error')
            return redirect(url_for('views.index'))
    return render_template("index.html")


@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        Firstname = request.form.get('Firstname')
        Lastname = request.form.get('Lastname')
        Username = request.form.get('Username')
        Password = request.form.get('Password')
        Checker = request.form.get('PWDChecker')
        Email = request.form.get('Email')
        
        user = User.query.filter_by(username=Username).first()
        
        if user:
            flash('Username already existed.', category='error')
        if Password != Checker:
            flash('Your password confirmation is failed, try it again.', category='error')
        else:
            new_user = User(firstname=Firstname, lastname=Lastname, username=Username, password=Password, email=Email)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('views.index'))
            
    return render_template("signup.html")

@auth.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")