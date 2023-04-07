from flask import Flask, redirect, url_for, render_template, send_file
from . import pieces, bids
from app.extensions.database import db, migrate



def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_extensions(app)
    register_blueprints(app)

    return app

# Blueprints
def register_blueprints(app: Flask):
    app.register_blueprint(pieces.routes.blueprint)
    app.register_blueprint(bids.routes.blueprint)

def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)