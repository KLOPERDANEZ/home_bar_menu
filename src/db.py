import io

from pymongo import MongoClient
from PIL import Image


class DBConnector:
    def __init__(self, config):
        self.config = config
        self.client = MongoClient(config["mongodb_connection_string"])
        self.collection = self.client.bar

    def update_item(self, item):
        self.collection.cocktail.insert_one(item)

    def update_img(self, img_id, contant):
        self.collection.images.insert_one({
            "type": "image",
            "img_id": img_id,
            "data": contant
        })

    def get_content(self):
        return self.collection.cocktail.find({"type": "cocktail"})

    def get_image(self, img_id):
        image_item = self.collection.images.find_one({"img_id": img_id})
        if image_item is not None:
            return image_item["data"]
        return b""
