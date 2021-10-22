from app import app

from flask import render_template


@app.route("/")
def index():
    return {
        'no_of_neurons': 3,
        'number of conections': 4,
        'name_of_the_network': "nome"
    }


@app.route("/about")
def about():
    return "<h1 style='color: red'> É sobre!!!!!!!!"
