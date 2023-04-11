from app.bids.models import Bid

def serialize_bids(bids):
    bids_list=[]

    for bid in bids:
        # if bid value is none, do not append to bids_list
        if bid.amount_of_bid is None:
            continue

        bids_list.append({
            "id": bid.id,
            "date" : bid.date.strftime("%Y-%m-%d %H:%M:%S") ,
            "user_name" : bid.user_name ,
            "country_of_origin" : bid.country_of_origin ,
            "user_email" : bid.user_email ,
            "piece_id" : bid.piece_id ,
            "amount_of_bid" : bid.amount_of_bid ,
            "letter" : bid.letter,
        })

    # sort Bids_list to have the highest bids on top
    sorted_list = sorted(bids_list, key=lambda x: x["amount_of_bid"], reverse=True)

    return sorted_list