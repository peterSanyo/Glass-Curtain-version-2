from flask import Blueprint, jsonify

blueprint = Blueprint("api", __name__)

@blueprint.get("/api/v1/bids")
def bids():
    return jsonify({
        "data" : "Hello World"
    })