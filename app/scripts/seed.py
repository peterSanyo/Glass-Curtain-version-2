from app.app import create_app
from app.pieces.models import Piece 
from app.extensions.database import db

if __name__ == "__main__":
    app = create_app()
    app.app_context().push()

pieces_data = {
  "era300" : {
        "name": "Era 300",
        "image_url1": "https://stadt-bremerhaven.de/wp-content/uploads/2023/02/Sonos-Era-300-Credenza-3.jpg",
        "image_url2": "https://media.sonos.com/images/znqtjj88/production/fe188ad4f111edbcf7402be9fa03168a19c18b77-3000x2011.jpg?w=3840&q=75&fit=clip&auto=format",
        "image_url3": "https://static.dezeen.com/uploads/2023/03/era-300-era-100-smart-speaker-sonos_dezeen_2364_col_11-1704x1318.jpg",
        "image_url4": "https://static.dezeen.com/uploads/2023/03/era-300-era-100-smart-speaker-sonos_dezeen_2364_col_18-1704x1118.jpg",
        "quote": ' "The most suffisticated product Sonos has built" ',
        "quoted":"Dana Krieger, head of Sonos",
        "offerer":"Sonos",
        "dimensions": "30x20x10cm",
        "materials": "hard case plastic and wood",
        "category":"Spatial home Audio",
        "price": "399$",
    },
    "phantom_syntopia" : {
        "name": "Phantom Syntopia",
        "image_url1": "https://www.numeromag.nl/wp-content/uploads/2023/03/Screenshot-2023-03-06-at-12.03.52.jpg",
        "image_url2": "https://cdn.motor1.com/images/mgl/g4JVP9/s1/rolls-royce-phantom-syntopia.webp",
        "image_url3": "https://www.rolls-roycemotorcars.com/content/dam/rrmc/marketUK/rollsroycemotorcars_com/phantom-syntopia/Phantom_Syntopia_Bonnet_D-07.jpg/jcr:content/renditions/cq5dam.web.1920.webp",
        "image_url4": "https://www.numeromag.nl/wp-content/uploads/2023/03/Screenshot-2023-03-06-at-12.03.52.jpg",
        "quote": ' "a state-of-the-art experience [...] by the forces of nature." ',
        "quoted":"Iris van Herpen",
        "offerer":"Rolls Royce X Iris van Herpen",
        "dimensions": "571x214x157 cm",
        "materials": "Leather, Fabric, Steel",
        "category":"Vehicle",
        "price": "-",
    },
    "white_fromme" : {
        "name": "White Fromme Collection",
        "image_url1": "https://media.madeindesign.com/nuxeo/products/f/c/stackable-bar-stool-fromme-white_madeindesign_406106_product800.jpg",
        "image_url2": "https://static.dezeen.com/uploads/2023/03/fromme-petite-friture-tom-chung_dezeen_2364_col_3-1704x959.jpg",
        "image_url3": "https://www.nostraforma.com/media/cache/1400x1400/002_petite_friture_vertigo_nova_140_ambient1_332df801d5c38d6072321536f64c5ed6.jpg",
        "image_url4": "https://media.madeindesign.com/nuxeo/products/f/c/stackable-bar-stool-fromme-white_madeindesign_406106_product800.jpg",
        "quote": ' "This design was inspired by the personal story of Tom Chung." ',
        "quoted":"Petite Friture, French Design Brand",
        "offerer":"Petite Friture X Tom Chang",
        "dimensions": "-",
        "materials": "Hardwearing Aluminium",
        "category":"Exclusive Furniture",
        "price": "-",
    },
    "color_palette" : {
        "name": "2023 Color Palette",
        "image_url1": "https://design-milk.com/images/2023/02/3form-2023-color-collection-09.jpg",
        "image_url2": "https://static.dezeen.com/uploads/2023/03/2023-color-collection-3form-design_dezeen_2364_col_8.jpeg",
        "image_url3": "https://static.dezeen.com/uploads/2023/03/3form-TB.jpg",
        "image_url4": "https://static.dezeen.com/uploads/2023/02/2023-color-collection-3form-design_dezeen_2364_hero2-1704x959.jpg",
        "quote": ' "This collection allowed us to be more introspective about the meaning of colour in our lives." ',
        "quoted":"Ryan Smith, chief creative of 3form",
        "offerer":"3form",
        "dimensions": "-",
        "materials": "Varia, Chroma and Glass",
        "category":"Modular Interiour Design ",
        "price": "-",
    }
}

for slug, piece in pieces_data.items():
    new_piece = Piece(
        slug=slug,
        name=piece["name"],
        image_url1=piece["image_url1"],
        image_url2=piece["image_url2"],
        image_url3=piece["image_url3"],
        image_url4=piece["image_url4"],
        quote=piece["quote"],
        quoted=piece["quoted"],
        offerer=piece["offerer"],
        dimensions=piece["dimensions"],
        materials=piece["materials"],
        category=piece["category"],
        price=piece["price"],
        )
    db.session.add(new_piece)

db.session.commit()