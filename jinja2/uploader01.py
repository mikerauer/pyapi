#!/usr/bin/python3

from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/uploader", methods = ["GET", "POST"])
def upload_file():
    if request.method == "POST":
        # creates file like object
        f = request.files["file"]
        # takes object and save to local system
        f.save(secure_filename(f.filename))
        return "file upload successful"

if __name__ == "__main__":
    app.run(port = 5006)

