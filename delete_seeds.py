# this is a file which is meant to be called when multiple seeds are stored in the Piece table of the database 

from app.app import db, create_app
from app.pieces.models import Piece

app=create_app()

def delete_seeds():
    # Replace YourModel with the appropriate model class in your application
    Piece.query.delete()
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        delete_seeds()
