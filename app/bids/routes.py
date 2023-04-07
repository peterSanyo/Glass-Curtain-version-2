from flask import Blueprint, render_template, request
from app.pieces.models import Piece
from app.bids.models import Bid

blueprint = Blueprint("bids", __name__)


@blueprint.get("/checkout")
def get_checkout():
    pieces = Piece.query.all()
    return render_template("bids/new.html", piece=pieces)

@blueprint.post("/checkout")
def post_checkout():

    bid = Bid()
    bid.save()

    pieces = Piece.query.all()
    return render_template("bids/new.html", piece=pieces)




# def create_order(form_data, pieces):

# # create Bid
#     bid = Bid()
#     bid.save()

#     bid = Bid(
#     user_name = request.form.get("user_name") ,
#     country_of_origin = request.form.get("country_of_origin") ,
#     user_email = request.form.get("user_email") ,

#     piece_id = request.form.get("piece_id") ,
#     amount_of_bid = request.form.get("amount_of_bid") ,
#     letter = request.form.get("letter")
#     )
#     bid.save()