from app.extensions.database import db 
from app.pieces.models import Piece

def test_piece_update(client):
    # updates cookie's properties
    # arrange
    piece = Piece(slug="era300", name="Era 300", price="399$") 
    # slug and name correct ?? 
    db.session.add(piece)
    db.session.commit()
    
    # act 
    piece.name = "Era 400"
    piece.save()

    # asses
    updated_piece = Piece.query.filter_by(name="Era 400").first()
    assert updated_piece.name == "Era 400"

def test_piece_delete(client):
    # deletes pieces
    piece=Piece(slug="phantom_syntopia", name="Phantom Syntopia", price="-")
    db.session.add(piece)
    db.session.commit()

    piece.delete()

    deleted_piece= Piece.query.filter_by(slug="phantom_syntopia").first()
    assert deleted_piece is None