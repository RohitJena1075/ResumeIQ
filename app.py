from flask import Flask
from routes.core import core
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(core)
    return app




