from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configure your app (database, blueprints, etc.)
    # ...

    app = Flask(__name__, template_folder='templates')

    return app

