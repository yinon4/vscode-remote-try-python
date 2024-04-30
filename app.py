from data import movies
from flask import Flask, render_template, request
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/movies/watchlist")
def watchlist():
    global movies
    watchlist = [movie for movie in movies if len(movie["reviews"]) == 0]

    return render_template("watchlist.html", movies=watchlist)

@app.route("/movies/watched")
def watched():
    global movies
    watched = [movie for movie in movies if len(movie["reviews"]) > 0]

    return render_template("watched.html", movies=watched)

@app.route("/movies/<string:movie_url>/review")
def review(movie_url):
    global movies
    movie = [movie for movie in movies if movie["url"] == movie_url][0]

    return render_template("review.html", movie=movie)

@app.route("/movies/<string:movie_url>/review", methods=["POST"])
def save_review(movie_url):
    global movies
    movie = [movie for movie in movies if movie["url"] == movie_url][0]
    print("MOVIE", movie)
    print("RATING", request.form["rating"])
    print("REVIEW", request.form["review"])

    return "Review saved"
