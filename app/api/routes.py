from flask import Blueprint, jsonify, request, render_template, redirect, url_for, current_app, render_template_string
from .services.serialize_bids import serialize_bids
from ..bids.models import Bid
from ..pieces.models import Piece
from app.extensions.database import db
from os import environ

blueprint = Blueprint("api", __name__)


@blueprint.get("/api/v1/admin")
def bids():
    if environ.get("API_KEY") == request.args.get("key"):
        bids = Bid.query.all()
        serialized_bids = serialize_bids(bids) 
        return render_template("bids/api.html", incoming_bids=serialized_bids)
    else:
         return jsonify({"error": "Invalid API key"}), 401
    
@blueprint.route("/run-seed")
# run seeds !
def run_seed():
    if not Piece.query.first():
        import app.scripts.seed
        return render_template_string("DATABASE SEED COMPLETED <a href='/'>Back to Gallery</a> \n \n <a href='/api/v1/admin'>To Admin Page</a>")
    else:
        return render_template_string("NOTHING TO RUN! <a href='/'>Back to Gallery</a> \n \n <a href='/api/v1/admin'>To Admin Page</a>")


@blueprint.route("/delete-seed")
def delete_seed():
    if not Piece.query.first():
        return render_template_string("Nothing to delete here \n <a href='/'>Back to Gallery</a> \n \n <a href='/api/v1/admin'>To Admin Page</a>")
    else:
        db.session.query(Piece).delete()
        db.session.commit()
        return render_template_string("SEEDS Deleted <a href='/'>Back to Gallery</a> \n \n <a href='/api/v1/admin'>To Admin Page</a>")


@blueprint.route("/api/v1/admin", methods=["GET", "POST"])
def update_pieces():
    if environ.get("API_KEY") == request.args.get("key"):
        if request.method == "POST":
            # Delete old Piece objects
            old_pieces = Piece.query.all()
            for piece in old_pieces:
                db.session.delete(piece)
            
            # Create 4 new Piece objects
            for i in range(4):
                name = request.form[f"name{i}"]
                image_url1 = request.form[f"img_url1{i}"]
                image_url2 = request.form[f"img_url2{i}"]
                image_url3 = request.form[f"img_url3{i}"]
                image_url4 = request.form[f"img_url4{i}"]
                quote = request.form[f"quote{i}"]
                quoted = request.form[f"quoted{i}"]
                offerer = request.form[f"offerer{i}"]
                dimensions = request.form[f"dimensions{i}"]
                materials = request.form[f"materials{i}"]
                category = request.form[f"category{i}"]
                price = request.form[f"price{i}"]
                
                new_piece = Piece(
                    name=name,
                    image_url1=image_url1, 
                    image_url2=image_url2, 
                    image_url3=image_url3,
                    image_url4=image_url4, 
                    quote=quote, 
                    quoted=quoted, 
                    offerer=offerer,
                    dimensions=dimensions,
                    materials=materials, 
                    category=category, 
                    price=price)
                db.session.add(new_piece)
            
            db.session.commit()
            return redirect("/")

