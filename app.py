"""Flask app for Cupcakes"""
from flask import Flask, jsonify

from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
  "postgresql://otherjoel:hello@13.57.9.123/otherjoel")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config['SECRET_KEY'] = "GET OUTTA MY DB!!!"

BASE_API_URL = '/api/cupcakes'

@app.get(BASE_API_URL)
def list_all_cupcakes():
    """
    Get data about all cupcakes

    Return JSON {'cupcakes': [{id, flavor, size, rating, image}, ...]}
    """

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized)

@app.get(f"{BASE_API_URL}/<int:cupcake_id>")
def list_single_cupcake(cupcake_id):
    """
    Get data about a single cupcake

    Return JSON {cupcake: {id, flavor, size, rating, image}}

    Raise 404 error if cupcake cannot be found
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)


