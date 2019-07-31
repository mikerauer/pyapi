#!/usr/bin/env python3

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    # returns the template populated
    return render_template("hellobasic.html")

@app.route('/<username>')
def userbuilder(username):
    return render_template('hellobasic2.html', coffee=username)

if __name__ == "__main__":
    app.run(port=5006)
