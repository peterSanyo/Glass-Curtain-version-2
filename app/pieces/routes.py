from flask import Blueprint, render_template, send_file, render_template_string, current_app
from .models import Piece
from app.extensions.database import db

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
# run seeds !
def run_seed():
    if not Piece.query.first():
        import app.scripts.seed
        return render_template_string("DATABASE SEED COMPLETED <a href='/'>Back to Gallery</a> \n \n <a href='/api/v1/admin'>To Admin Page</a>")
    else:
        return render_template_string("NOTHING TO RUN! <a href='/'>Back to Gallery</a> \n \n <a href='/api/v1/admin'>To Admin Page</a>")


@blueprint.route("/delete-seed")
def delete_seed():
    if not Piece.query.first():
        return render_template_string("Nothing to delete here \n <a href='/'>Back to Gallery</a> \n \n <a href='/api/v1/admin'>To Admin Page</a>")
    else:
        db.session.query(Piece).delete()
        db.session.commit()
        return render_template_string("SEEDS Deleted <a href='/'>Back to Gallery</a> \n \n <a href='/api/v1/admin'>To Admin Page</a>")