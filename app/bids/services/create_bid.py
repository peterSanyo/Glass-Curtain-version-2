from app.bids.models import Bid
from app.pieces.models import Piece

def create_bid(form_data, pieces):
    # create piece
    piece=Piece()
    piece.save()

    # create bid !
    bid = Bid(
        user_name = form_data.get("user_name") ,
        country_of_origin = form_data.get("country_of_origin") ,
        user_email = form_data.get("user_email") ,

        piece_id = form_data.get("piece_id") ,
        amount_of_bid = form_data.get("amount_of_bid") ,
        letter = form_data.get("letter"),

        piece=piece
    )
    bid.save()
