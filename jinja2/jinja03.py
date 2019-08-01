#!/usr/bin/python3

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/astros")
def astros():
    mydata = requests.get('http://api.open-notify.org/astros.json')
    isspeople = mydata.json()
    return render_template("myastros.html", people=isspeople['people'])

@app.route("/scoretest/<int:score>")
def passfail(score):
   return render_template("highscore.html", marks = score)

if __name__ == "__main__":
    app.run(port=5006)
