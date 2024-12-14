from flask import Flask, render_template, Blueprint, redirect, url_for, Blueprint
from jinja2 import TemplateNotFound
from flask_migrate import Migrate
from flask_login import login_required, current_user
from . import db


main = Blueprint('main', __name__,
                        template_folder='templates')

@main.route('/', defaults={'page': 'home'})
@main.route('/home')
def show(page):
    try:
        return render_template(f'main/{page}.html')
    except TemplateNotFound:
        return render_template('404.html'), 404


@main.route('/cloud')
@login_required
def cservices():
    return render_template('cloud.html')


@main.route('/ics')
@login_required
def ics():
    return render_template('ics.html')


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


migrate = Migrate(main, db)
