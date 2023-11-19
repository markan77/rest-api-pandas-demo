from flask import Flask
from flask.json import jsonify

app = Flask(__name__)  # Flask("main.py")

dict_primjer = {
    "Ime": "Marko",
    "Prezime": "Markic",
    "Email": "marko@mail.com"
}

@app.route("/")
def home():
    return "<h1><a href='/about'>Home page</a></h1>"

@app.route("/about")
def about():
    return "<p>About page</p>"

@app.route("/user/<username>")
def user(username):
    return f"<h3>User page for: {username}</h3>"

@app.route("/json")
def json():
    return jsonify(dict_primjer)

@app.route("/json/<key>")
def json_value(key):
    return dict_primjer.get(key, "Unknown key")
