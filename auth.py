from flask import Blueprint,request,render_template,redirect,url_for,flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .__init__ import db
from flask_login import login_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html',title='Login')
    else:
        email = request.form.get('user')
        password = request.form.get('password')

        user_data = User.query.filter_by(email=email).first()

        if not user_data:
            flash('Please sign up before!')
            return redirect(url_for('auth.signup'))
        elif not check_password_hash(user_data.password, password):
            flash('Please check your login details and try again.')
    login_user(user_data)
    return redirect(url_for('main.index'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method=='GET':
        return render_template('signUp.html')
    else:
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('Incorect Password')
            return redirect(url_for('auth.signup'))

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))
        
        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    

