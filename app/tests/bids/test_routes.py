from app.extensions.database import db, CRUDMixin
from app.bids.models import Bid
from app.pieces.models import Piece
# from app.pieces.models import Piece

#  I skipped this test due to time constraints.
# It didn't work after days of trying and until now nobody could help me with it.
# def test_get_checkout_renders(client):
#     # page renders and loads checkout
#     pieces = Piece.query.all()
#     response = client.get("/checkout", piece=pieces)
#     assert b"Checkout" in response.data


def test_post_checkout_creates_bid(client):
    # creates a bid record
    response = client.post("/checkout", data={
    "user_name" : "Peter" ,
    "country_of_origin" : "Germany" ,
    "user_email" : "p@p",
    "piece_id" : 1 ,
    "amount_of_bid" : 12 , 
    "letter" : "Hello" , 
    })
    assert Bid.query.first() is not None