from app.extensions.database import db, CRUDMixin
from datetime import datetime

class Bid(db.Model, CRUDMixin):
    __tablename__ = "bid"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user_name = db.Column(db.String(40))
    country_of_origin = db.Column(db.String(40))
    user_email = db.Column(db.String(40))

    piece_id = db.Column(db.Integer, db.ForeignKey("piece.id"))
    amount_of_bid = db.Column(db.Numeric(10, 2))
    letter = db.Column(db.String(3000))

    piece = db.relationship("Piece", backref="bid", lazy=True )