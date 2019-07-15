'''
 Created by skywalkeryin on 7/15/2019
'''


from flask import Flask
from flask_migrate import Migrate

migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')

    # register blue print
    register_blueprint(app)
    # register plugin
    register_plugin(app)

    return app


def register_blueprint(app):

    from app.api.v1 import create_blueprint
    app.register_blueprint(create_blueprint(), url_prefix='/v1')


def register_plugin(app):
    # register sqlalchemy
    from app.models.base import db

    from app.models.user import User #added here for migrate detected

    db.init_app(app)
    # register migrate
    migrate.init_app(app, db)

