from flask import Flask

from .config import Config
from .auth import register_auth
from .db import register_db
from .routes import register_routes


def create_app():
    app = Flask(__name__)
    app.secret_key = Config.APP_SECRET_KEY
    register_auth(app)
    register_db(app)
    register_routes(app)
    return app
