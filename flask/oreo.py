#!/usr/bin/python3

from flask import Flask, make_response, request, render_template, redirect, url_for

app = Flask(__name__)

# entry point for our users
# renders a template that asks for their name
# index.html points to /setcookie
@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")

# set the cookie and send it back to the user
@app.route("/setcookie", methods = ["POST", "GET"])
def setcookie():
    if request.method == "POST":
        user = request.form["nm"]

        # Note that cookies are set on response objects.
        # Since you normally just return strings
        # Flask will convert them into response objects for you
        resp = make_response(render_template("readcookie.html"))
        # add a cookie to our response object
                   #cookievar #value
        resp.set_cookie("userID", user)
#    else:
#        redirect(url_for("index")
#execpt....
        # return our response object includes our cookie
    return resp

# check users cookie for their name
@app.route("/getcookie")
def getcookie():
    try:
        name = request.cookies.get("userID")
        return '<h1>welcome '+name+'</h1>'
    except TypeError:
        redirect(url_for("index"))


if __name__ == "__main__":
    app.run(port=5006)
