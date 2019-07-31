#!/usr/bin/python3

#!/usr/bin/env python3
from flask import Flask, redirect, url_for

# best practice is to split each one and not , them
#from flask import redirect
#from flask import url_for

app = Flask(__name__)

@app.route("/admin")
def hello_admin():
    return "Hello Admin\n"

@app.route("/guest/<guest>")
def hello_guest(guest):
    # return "Hello %s as Guest" % guest
    return f'Hello {guest} Guest\n'
    # return "Hello {} Guest".format(guest)

@app.route("/user/<name>")
def hello_user(name):
    # redirects the name to the admin or gues func
    if name =="admin":
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for("hello_guest",guest = name))

if __name__ == "__main__":
    app.run(port=5006, debug = True)
