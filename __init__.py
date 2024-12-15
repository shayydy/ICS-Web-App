from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .app_factory import create_app
from .models import User
from flask_bcrypt import Bcrypt
import os

# Create the Flask app instance
app = Flask(__name__)

# Configure the app
app.config['SECRET_KEY'] = '1b9fac1236cc63bc46649867a4b3dd8d'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.db'

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(db.select(User).filter_by(id=1)).scalar()

# Register blueprints
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

# Create database tables if they don't exist
with app.app_context():
    db.create_all()
