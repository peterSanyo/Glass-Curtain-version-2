from flask import Blueprint, jsonify
from .services.serialize_bids import serialize_bids
from ..bids.models import Bid

blueprint = Blueprint("api", __name__)

@blueprint.get("/api/v1/bids")
def bids():
    bids=Bid.query.all()

    return jsonify(
        serialize_bids(bids)
    )

