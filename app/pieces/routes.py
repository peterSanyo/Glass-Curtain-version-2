from flask import Blueprint, render_template, send_file
from .models import Piece

blueprint = Blueprint("pieces", __name__)

@blueprint.route("/")
def index():
    # index page
    all_pieces=Piece.query.all()
    return render_template("index.html", piece=all_pieces)


@blueprint.route("/download")
def download():
    # download exhibit material
    return send_file("static/downloads/exhibition.txt", as_attachment=True)

