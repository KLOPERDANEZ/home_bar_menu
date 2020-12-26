from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    items = [
        {
            "name": "Негрони",
            "strong": "Крепкий",
            "description": "Красненький",
            "image_file": "negroni.jpg",
            "general_ingredients": ["Джин", "Красный вермут", "Кампари"],
            "additional_ingredients": ["Цедра апельсина"],
            "comment": "Цедра апельсина используется для украшения и для добавления аромата в напиток",
        }
    ]
    return render_template("content.html", items=items)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run()

