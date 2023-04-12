from flask import Blueprint, render_template, send_file
from .models import Piece

blueprint = Blueprint("pieces", __name__)

@blueprint.route("/")
def index():
    # index page
    all_pieces=Piece.query.all()
    print(all_pieces)
    return render_template("index/index.html", pieces=all_pieces)


@blueprint.route("/exhibit/<slug>")
def piece(slug):
    # product pages
  piece= Piece.query.filter_by(slug=slug).first_or_404()
  return render_template("pieces/product_page.html", piece=piece)

@blueprint.route("/download")
def download():
    # download exhibit material
    return send_file("static/downloads/exhibition.txt", as_attachment=True)

@blueprint.route("/run-seed")
def run_seed():
    if not Piece.query.filter_by(slug="era300").first():
        import app.scripts.seed
        return "Database seed completed!"
    else:
        return "Nothing to run."