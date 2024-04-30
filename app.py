#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask, render_template, request
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# @app.route("/")
# def hello():
#     session["count"] = 0
#     return render_template("index.html", count=session.get("count", 0))

# @app.route("/increment")
# def increment():
#     session["count"] = session.get("count", 0) + 1
#     return session["count"].__str__()

movies = [
    {"id": 1, "title": "The Shawshank Redemption", "year": 1994, "length": 142, "url": "the-shawshank-redemption", "reviews": [{"rating": 4, "review": "Great movie", "date": "2021-01-01"}]},
    {"id": 2, "title": "The Godfather", "year": 1972, "length": 175, "url": "the-godfather", "reviews": [{"rating": 5, "review": "Best movie ever", "date": "2021-01-01"}]},
    {"id": 3, "title": "The Dark Knight", "year": 2008, "length": 152, "url": "the-dark-knight", "reviews": [{"rating": 4, "review": "Great movie", "date": "2021-01-01"}]},
    {"id": 4, "title": "The Godfather: Part II", "year": 1974, "length": 202, "url": "the-godfather-part-ii", "reviews": [{"rating": 5, "review": "Best movie ever", "date": "2021-01-01"}]},
    {"id": 5, "title": "The Lord of the Rings: The Return of the King", "year": 2003, "length": 201, "url": "the-lord-of-the-rings-the-return-of-the-king", "reviews": [{"rating": 4, "review": "Great movie", "date": "2021-01-01"}]},
    {"id": 6, "title": "Pulp Fiction", "year": 1994, "length": 154, "url": "pulp-fiction", "reviews": [{"rating": 5, "review": "Best movie ever", "date": "2021-01-01"}]},
    {"id": 7, "title": "The Good, the Bad and the Ugly", "year": 1966, "length": 161, "url": "the-good-the-bad-and-the-ugly", "reviews": [{"rating": 4, "review": "Great movie", "date": "2021-01-01"}]},
    {"id": 8, "title": "The Lord of the Rings: The Fellowship of the Ring", "year": 2001, "length": 178, "url": "the-lord-of-the-rings-the-fellowship-of-the-ring", "reviews": [{"rating": 5, "review": "Best movie ever", "date": "2021-01-01"}]},
    {"id": 9, "title": "Fight Club", "year": 1999, "length": 139, "url": "fight-club", "reviews": [{"rating": 4, "review": "Great movie", "date": "2021-01-01"}]},
    {"id": 10, "title": "Forrest Gump", "year": 1994, "length": 142, "url": "forrest-gump", "reviews": [{"rating": 5, "review": "Best movie ever", "date": "2021-01-01"}]},
    {"id": 11, "title": "Inception", "year": 2010, "length": 148, "url": "inception", "reviews": [{"rating": 4, "review": "Great movie", "date": "2021-01-01"}]},
    {"id": 12, "title": "The Lord of the Rings: The Two Towers", "year": 2002, "length": 179, "url": "the-lord-of-the-rings-the-two-towers", "reviews": [{"rating": 5, "review": "Best movie ever", "date": "2021-01-01"}]},
    {"id": 13, "title": "Star Wars: Episode V - The Empire Strikes Back", "year": 1980, "length": 124, "url": "the-empire-strikes-back", "reviews": [{"rating": 4, "review": "Great movie", "date": "2021-01-01"}]},
    {"id": 14, "title": "The Matrix", "year": 1999, "length": 136, "url": "the-matrix", "reviews":[{"rating": 5, "review": "Best movie ever", "date": "2021-01-01"}]},
    {"id": 15, "title": "Goodfellas", "year": 1990, "length": 146, "url": "goodfellas", "reviews": [{"rating": 4, "review": "Great movie", "date": "2021-01-01"}]},
    {"id": 16, "title": "One Flew Over the Cuckoo's Nest", "year": 1975, "length": 133, "url": "one-flew-over-the-cuckoos-nest", "reviews": []},
    {"id": 17, "title": "Seven Samurai", "year": 1954, "length": 207, "url": "seven-samurai", "reviews": []},
    {"id": 18, "title": "Se7en", "year": 1995, "length": 127, "url": "se7en", "reviews": [{"rating": 5, "review": "Best movie ever", "date": "2021-01-01"}]},
    {"id": 19, "title": "City of God", "year": 2002, "length": 130, "url": "city-of-god", "reviews": []},
    {"id": 20, "title": "Life Is Beautiful", "year": 1997, "length": 116, "url": "life-is-beautiful", "reviews": []},
    {"id": 21, "title": "The Silence of the Lambs", "year": 1991, "length": 118, "url": "the-silence-of-the-lambs", "reviews": [{"rating": 4, "review": "Great movie", "date": "2021-01-01"}]},
    {"id": 22, "title": "It's a Wonderful Life", "year": 1946, "length": 130, "url": "its-a-wonderful-life", "reviews": []},
    {"id": 23, "title": "Star Wars: Episode IV - A New Hope", "year": 1977, "length": 121, "url": "star-wars-episode-iv-a-new-hope", "reviews": [{"rating": 4, "review": "Great movie", "date": "2021-01-01"}]},
    ]


@app.route("/movies/watchlist")
def watchlist():
    global movies
    watchlist = [movie for movie in movies if len(movie["reviews"]) == 0]
    return render_template("watchlist.html", movies=watchlist)

@app.route("/movies/watched")
def watched():
    global movies
    watched = [movie for movie in movies if len(movie["reviews"]) > 0]

    return render_template("watched.html", movies=movies)

@app.route("/movies/<string:movie_url>/review")
def review(movie_url):
    global movies
    movie = [movie for movie in movies if movie["url"] == movie_url][0]

    return render_template("review.html", movie=movie)

@app.route("/movies/<string:movie_url>/review", methods=["POST"])
def save_review(movie_id):
    global movies
    movie = [movie for movie in movies if movie["id"] == movie_id][0]
    print("MOVIE", movie)
    print("RATING", request.form["rating"])
    print("REVIEW", request.form["review"])

    return "Review saved"
