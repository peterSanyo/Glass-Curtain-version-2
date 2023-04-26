from flask import Blueprint, render_template, request, current_app
from app.pieces.models import Piece
from .services.create_bid import create_bid

blueprint = Blueprint("bids", __name__)


@blueprint.get("/checkout")
def get_checkout():
    pieces = Piece.query.all()
    return render_template("bids/new.html", pieces=pieces)

@blueprint.post("/checkout")
def post_checkout():
    try:
        pieces = Piece.query.all()

        if not all([
            request.form.get("user_name"),
            request.form.get("country_of_origin"),
            request.form.get("user_email"),
            request.form.get("piece_id"),
            request.form.get("amount_of_bid"),
            request.form.get("letter")
        ]):
            raise Exception("Please fill out all fields.")

        create_bid(request.form, pieces)
        return render_template("bids/new.html", pieces=pieces)
    
    except Exception as error_message:
        error = error_message or "An error occured while processing your order. Please make sure to enter valid data."
        
        current_app.logger.info(f"Error creating a bid: {error}")

        return render_template("bids/new.html",
        piece=pieces,
        error=error
        )