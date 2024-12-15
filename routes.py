from flask import render_template, url_for, flash, redirect
from webapp.forms import RegistrationForm, LoginForm
from webapp.models import User, Post
from webapp import app
from jinja2 import TemplateNotFound
from flask_login import login_required, current_user
from flask_migrate import Migrate
from . import db


posts = [
    {
        'author': 'Shay Long',
        'title': 'The endlessness of my failures',
        'content': 'I cannot beleive this still is not working',
        'date_posted': '20241214'
    },
    {
        'author': 'Shay Long',
        'title': 'It has to work eventually',
        'content': 'Right?',
        'date_posted': '20241214'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html') 


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route('/ics')  
def ics():
    # Your route logic for generating the ICS file goes here
    return render_template('ics.html', title='ICS Results')


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/cloud')
def cloud():
    return render_template('cloud.html', title='Cloud Services')


@app.route('/profile')
def profile():
    return render_template('profile.html', name=current_user.name)


migrate = Migrate(app, db)