from app.extensions.database import db

class Piece(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80), unique=True)
    image_url1 = db.Column(db.String(400))
    image_url2 = db.Column(db.String(400))
    image_url3 = db.Column(db.String(400))
    image_ur4 = db.Column(db.String(400))
    quote = db.Column(db.String(80), unique=True)
    quoted = db.Column(db.String(80))
    offerer = db.Column(db.String(80))
    dimensions = db.Column(db.String(80))
    materials = db.Column(db.String(80))
    category = db.Column(db.String(80))
    price = db.Column(db.String(10))
    count = db.Column(db.Integer, unique=True)

    piece_bids = db.relationship("Bid", backref="piece", lazy=True)