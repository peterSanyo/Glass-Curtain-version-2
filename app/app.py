from flask import Flask, redirect, url_for, render_template, send_file
from . import pieces



def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_blueprints(app)

    return app

# Blueprints
def register_blueprints(app: Flask):
    app.register_blueprint(pieces.routes.blueprint)
