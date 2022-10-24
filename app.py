"""Flask app for Cupcakes"""
from crypt import methods
from flask import Flask, jsonify, request

from models import db, connect_db, Cupcake

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = (
#   "postgresql://otherjoel:hello@13.57.9.123/otherjoel")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "GET OUTTA MY DB!!!"

CUPCAKES_ENDPOINT = '/api/cupcakes'

@app.get(CUPCAKES_ENDPOINT)
def list_all_cupcakes():
    """
    Get data about all cupcakes

    Return JSON {'cupcakes': [{id, flavor, size, rating, image}, ...]}
    """

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.get(f"{CUPCAKES_ENDPOINT}/<int:cupcake_id>")
def list_single_cupcake(cupcake_id):
    """
    Get data about a single cupcake

    Return JSON {cupcake: {id, flavor, size, rating, image}}

    Raise 404 error if cupcake cannot be found
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


@app.post(CUPCAKES_ENDPOINT)
def create_new_cupcake():
    """
    Collect flavor, size, rating, and image URL from the form.

    Check if image URL is empty, and if so use default image URL provided
    in models.py

    Add new cupcake to database

    Return JSON {cupcake: {id, flavor, size, rating, image}}
    """

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"] or None

    new_cupcake = Cupcake(
        flavor=flavor,
        size=size,
        rating=rating,
        image=image,
    )

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)


#### Comment out below for code review

# @app.patch(f"{CUPCAKES_ENDPOINT}/<int:cupcake_id>")
# def update_cupcake_info(cupcake_id):
#     """
#     Update cupcake info
#     """
    
#     cupcake = Cupcake.query.get_or_404(cupcake_id)


