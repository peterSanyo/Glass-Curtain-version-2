from flask import Blueprint, jsonify, request, render_template
from .services.serialize_bids import serialize_bids
from ..bids.models import Bid
from os import environ

blueprint = Blueprint("api", __name__)


@blueprint.get("/api/v1/bids")
def bids():
    if environ.get("API_KEY") == request.args.get("key"):
        bids=Bid.query.all()
        incomin_bids = jsonify(
            serialize_bids(bids)
            )
        return render_template("bids/api.html", incoming_bids=incomin_bids)
    else:
        return jsonify({"error": "Invalid API key"}), 401

