from app.extensions.database import db, CRUDMixin

class Piece(db.Model, CRUDMixin):
    __tablename__ = "piece"
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80))
    name = db.Column(db.String(80))
    image_url1 = db.Column(db.String(400))
    image_url2 = db.Column(db.String(400))
    image_url3 = db.Column(db.String(400))
    image_url4 = db.Column(db.String(400))
    quote = db.Column(db.String(80))
    quoted = db.Column(db.String(80))
    offerer = db.Column(db.String(80))
    dimensions = db.Column(db.String(80))
    materials = db.Column(db.String(80))
    category = db.Column(db.String(80))
    price = db.Column(db.String(10))