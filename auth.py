from flask import render_template, url_for, flash, redirect, request, Blueprint
from . import app, db, bcrypt
from webapp.forms import RegistrationForm, LoginForm
from webapp.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


auth = Blueprint('auth', __name__)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
