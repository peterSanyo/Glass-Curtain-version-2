from flask import Blueprint, render_template, request
from app.pieces.models import Piece
from .services.create_bid import create_bid

blueprint = Blueprint("bids", __name__)


@blueprint.get("/checkout")
def get_checkout():
    pieces = Piece.query.all()
    return render_template("bids/new.html", piece=pieces)

@blueprint.post("/checkout")
def post_checkout():
    pieces = Piece.query.all()

    create_bid(request.form, pieces)

    return render_template("bids/new.html", piece=pieces)