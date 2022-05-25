"""from crypt import methods
from flask import Blueprint, jsonify, request
from .models import Movie
from flask_cors import CORS, cross_origin

main = Blueprint("main", __name__)

CORS(main, support_credentials=True)


@main.route("/add_movie", methods=["POST"])
@cross_origin(supports_credentials=True)
def add_movie():

    movie_data = request.get_json(force=True)

    return Movie(movie_data["number1"], movie_data["number2"]), 200
"""
