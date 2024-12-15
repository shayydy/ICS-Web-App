from flask import Flask, render_template, Blueprint, redirect, url_for, Blueprint
from jinja2 import TemplateNotFound
from flask_migrate import Migrate
from flask_login import login_required, current_user
from . import db


main = Blueprint('main', __name__,
                        template_folder='templates')

migrate = Migrate(main, db)
