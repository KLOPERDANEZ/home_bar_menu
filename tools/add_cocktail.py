import io
from random import random

from PIL import Image

from src.db import DBConnector

if __name__ == '__main__':

    image_id = int(random() * 1000)

    db_connector = DBConnector({"mongodb_connection_string": "mongodb://127.0.0.1:27017"})
    cocktail = {
        "name": "Джин-тоник",
        "strong": "Средний",
        "description": "Классический коктейль",
        "general_ingredients": ["Джин", "Тоник", "Лаймовый сок"],
        "additional_ingredients": ["Лайм", "Огурец"],
        "comment": "Классический, но оттого не менее прикольный коктейль",
    }

    cocktail.update({
        "id": str(image_id),
        "type": "cocktail",
        "image_file": image_id,
    })

    db_connector.update_item(cocktail)

    im = Image.open("/home/mkarpunkin/kola.jpeg")

    image_bytes = io.BytesIO()
    im.save(image_bytes, format='JPEG')

    db_connector.update_img(image_id, image_bytes.getvalue())
