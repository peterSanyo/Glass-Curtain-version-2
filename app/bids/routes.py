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

    if not all([
        request.form.get("user_name"),
        request.form.get("country_of_origin"),
        request.form.get("user_email"),
        request.form.get("piece_id"),
        request.form.get("amount_of_bid"),
        request.form.get("letter")
    ]):
        return render_template("bids/new.html",
        piece=pieces,
        error = "Please fill out the whole form to place a valid bid."
        )

    create_bid(request.form, pieces)
    return render_template("bids/new.html", piece=pieces)