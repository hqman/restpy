import os


import click
from flask  import Flask, url_for ,jsonify, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, '../test.db')


def create_app(config_name):
    """Create an application instance."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SERVER_NAME'] = 'localhost'
    db.init_app(app)

     # register blueprints
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')


    return app