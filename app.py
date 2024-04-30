#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask, render_template, session, request
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def hello():
    session["count"] = 0
    return render_template("index.html", count=session.get("count", 0))

@app.route("/increment")
def increment():
    session["count"] = session.get("count", 0) + 1
    return session["count"].__str__()


@app.route("/movies")
def movies():
    session["movies"] = [
    {"id": 1, "title": "The Shawshank Redemption", "year": 1994, "length": 142, "rating": 4},
    {"id": 2, "title": "The Godfather", "year": 1972, "length": 175, "rating": 5},
    {"id": 3, "title": "The Dark Knight", "year": 2008, "length": 152, "rating": 4},
    {"id": 4, "title": "The Godfather Part II", "year": 1974, "length": 202, "rating": 5},
    ]
    movies =session.get("movies", [])
    return render_template("movies.html", movies=movies)

@app.route("/movies/<int:movie_id>/review")
def review(movie_id):
    movies = session.get("movies", [])
    movie = [movie for movie in movies if movie["id"] == movie_id][0]

    return render_template("review.html", movie=movie)

@app.route("/movies/<int:movie_id>/review", methods=["POST"])
def save_review(movie_id):
    print("RATING", request.form["rating"])
    print("REVIEW", request.form["review"])
    movies = session.get("movies", [])
    movie = [movie for movie in movies if movie["id"] == movie_id][0]

    return "Review saved"
