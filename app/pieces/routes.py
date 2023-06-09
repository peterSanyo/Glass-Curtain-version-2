from flask import Blueprint, render_template, send_file
from .models import Piece
from app.extensions.database import db

blueprint = Blueprint("pieces", __name__)

@blueprint.route("/")
def index():
    # index page
    all_pieces=Piece.query.all()
    print(all_pieces)
    return render_template("index/index.html", pieces=all_pieces)


@blueprint.route("/exhibit/<int:id>")
def piece(id):
    # product pages
  piece= Piece.query.filter_by(id=id).first_or_404()
  return render_template("pieces/product_page.html", piece=piece)

@blueprint.route("/download")
def download():
    # download exhibit material
    return send_file("static/downloads/exhibition.txt", as_attachment=True)

