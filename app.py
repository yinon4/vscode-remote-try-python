#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask, render_template, session
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