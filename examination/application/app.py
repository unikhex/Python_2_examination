from flask import Flask, render_template,request
import urllib.request
import ssl
import json
import pandas as pd
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

@app.route("/api", methods=["POST"])
def api_post():
    ÅR = request.form["year"]
    MÅNAD = request.form["month"]
    DAG=request.form["day"]

    context = ssl._create_unverified_context()
    data_url = f"https://www.elprisetjustnu.se/elpris-api"
    json_data = urllib.request.urlopen(data_url,context=context).read()
    data = json.loads(json_data)
    df = pd.DataFrame(data)
    table_data = df.to_html(columns=["date","localName"],classes="table p-5",justify="left")
    return render_template("index.html",data=table_data)



