from flask import Flask
from flask_restx import Api

from config import Config
from database import db
from view.auth import auth_ns
from view.directors import director_ns
from view.genres import genre_ns
from view.movies import movie_ns
from view.users import user_ns


def create_app(config):
    application = Flask(__name__)
    application.config.from_object(config)
    configure_app(application)

    return application


def configure_app(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


def create_data(app, db):
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    create_data(app, db)
    app.run()
