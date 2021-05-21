from flask import Flask, redirect, render_template, request

from helpers import error

app = Flask(__name__)

@app.route("/")
def index():
    return error("Too much Kool-Aid")
    # return render_template("index.html.j2")
    # return render_template("test.html")

