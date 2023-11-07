from flask import Flask, render_template,request,jsonify
import urllib.request
import ssl
import json
import pandas as pd
import requests


app = Flask(__name__)

@app.route("/api", methods=["GET","POST"])
def el_pris():
    if request.method == "POST":
        year = request.form.get("year")
        month = request.form.get("month")
        day=request.form.get("day")
        price_class = request.form("price_class")
        api_url = f"https://www.elprisetjustnu.se/api/v1/prices/{year}/{month}-{day}_{price_class}.json"
        response = requests.get(api_url)

        if response.status_code == 200:
            electricity_price = response.json()
            return render_template("prices.html",electricity_price)
        else:
            error_message = ("Error fetching electicity prices")
            return render_template("error.html",error_message=error_message)
        
    return render_template("index.html")

if __name__== "__main__":
    app.run(debug=True)


    


