from flask import Blueprint, render_template, send_file
from .models import Piece

blueprint = Blueprint("pieces", __name__)

pieces_data = {
    "era300" : {
        "name": "Era 300",
        "image_url": "https://stadt-bremerhaven.de/wp-content/uploads/2023/02/Sonos-Era-300-Credenza-3.jpg",
        "quote": ' "The most suffisticated product Sonos has built" ',
        "quoted":"Dana Krieger, head of Sonos",
        "offerer":"Sonos",
        "dimensions": "30x20x10 cm",
        "materials": "hard case plastic and wood",
        "category":"Spatial home Audio",
        "price": "399$",
        "count": 1 
    },
    "phantom_syntopia" : {
        "name": "Phantom Syntopia",
        "image_url": "https://cdn.motor1.com/images/mgl/g4JVP9/s1/rolls-royce-phantom-syntopia.webp",
        "quote": ' "a state-of-the-art experience [...] by the forces of nature." ',
        "quoted":"Iris van Herpen",
        "offerer":"Rolls Royce X Iris van Herpen",
        "dimensions": "571x214x157 cm",
        "materials": "Leather, Fabric, Steel",
        "category":"Vehicle",
        "price": "-",
        "count": 2
    },
    "white_fromme" : {
        "name": "White Fromme Collection",
        "image_url": "https://static.dezeen.com/uploads/2023/03/fromme-petite-friture-tom-chung_dezeen_2364_col_3-1704x959.jpg",
        "quote": ' "This design was inspired by the personal story of Tom Chung." ',
        "quoted":"Petite Friture, French Design Brand",
        "offerer":"Petite Friture X Tom Chang",
        "dimensions": "-",
        "materials": "Hardwearing Aluminium",
        "category":"Exclusive Furniture",
        "price": "-",
        "count": 3
    },
    "color_palette" : {
        "name": "2023 Color Palette",
        "image_url": "https://static.dezeen.com/uploads/2023/02/2023-color-collection-3form-design_dezeen_2364_hero2-1704x959.jpg",
        "quote": ' "This collection allowed us to be more introspective about the meaning of colour in our lives." ',
        "quoted":"Ryan Smith, chief creative of 3form",
        "offerer":"3form",
        "dimensions": "-",
        "materials": "Varia, Chroma and Glass",
        "category":"Modular Interiour Design ",
        "price": "-",
        "count": 4
    }
}

@blueprint.route("/")
def index():
    # index page
    return render_template("index.html")


@blueprint.route("/download")
def download():
    # download exhibit material
    return send_file("static/downloads/exhibition.txt", as_attachment=True)

