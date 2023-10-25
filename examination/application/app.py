from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    """This is the main page. Where you are first directed to
    """
    return render_template("index.html")

@app.route("/form")
def form():
    """This is where my form html site is rendered
    """
    return render_template("form.html")


