from flask import Flask, render_template, send_file, stream_with_context, make_response

from src.db import DBConnector


class Handler:

    def __init__(self, config: dict, db_connector: DBConnector, app: Flask):
        self.config = config
        self.db_connector = db_connector
        self.app = app
        self.registration_endpoints()

    def registration_endpoints(self):

        @self.app.route("/")
        def home():
            items = self.get_content()
            if items is not None:
                return render_template("content.html", items=items)
            return render_template("content.html")

        @self.app.route("/about")
        def about():
            return render_template("about.html")

        @self.app.route("/img/<int:pid>")
        def get_image(pid: int):
            image_binary = self.db_connector.get_image(pid)
            response = make_response(image_binary)
            response.headers.set("Content-Type", "image/jpeg")
            return response

    def get_content(self):
        content = self.db_connector.get_content()
        if content.count():
            return list(content)
        return None

    def run(self):
        self.app.run(host=self.config["host"], port=self.config["port"], debug=self.config["debug_mode"])


def load_config():
    return {
        "host": "0.0.0.0",
        "port": 5000,
        "debug_mode": True,
        "mongodb_connection_string": "mongodb://127.0.0.1:27017"
    }


if __name__ == "__main__":
    config = load_config()
    db_connector = DBConnector(config)
    app = Flask(__name__)
    handler = Handler(config, db_connector, app)
    handler.run()

