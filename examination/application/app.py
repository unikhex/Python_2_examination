from flask import Flask, render_template,request
import pandas as pd
import requests
from urllib.error import HTTPError
from datetime import datetime,timedelta

app = Flask(__name__)

def json_data_to_pandas_df(api_url):
    """Converts json data to a pandas dataframe"""
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame(data)
        return df
    except HTTPError as e:
        return e
    except Exception as e:
        return e

def pandas_df_to_html_table(api_url, columns=None):
    """Converts the datafrme to a html table"""
    try:
        df = json_data_to_pandas_df(api_url)

        if isinstance(df, HTTPError):
            return None

        df.drop(df.columns[2], axis=1, inplace=True)
        df.drop(df.columns[3], axis=1, inplace=True)
        df.columns = ["SEK per KWH", "EUR per KWH", "Tid"]
        df['Tid'] = pd.to_datetime(df['Tid'])
        df['Tid'] = df['Tid'].dt.strftime('%H:%M')

        if columns is None:
            table_data = df.to_html(classes="table p-5", justify="left")
        else:
            table_data = df.to_html(columns=columns, classes="table p-5", justify="left")

        return table_data
    except HTTPError as e:
        return e
    except Exception as e:
        return e
    
    
def get_max_date():
    """Decides the max date for my app.given today's date"""
    date = datetime.today()
    new_date = date + timedelta(days=1)
    day = new_date.day
    month = new_date.month
    year = new_date.year
    max_date = f"{year}-{month:02d}-{day:02d}"
    
    return max_date


@app.route("/")
def index():
    """Main page and the page one returns to if connected wrongly"""
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api_post():
    """function that is called after filling in the dates and priceclass"""
    try:
        date = request.form["date"]
        year, month, day = date.split('-')
        priceclass = request.form["prisklass"]
        api_url = f"https://www.elprisetjustnu.se/api/v1/prices/{year}/{month}-{day}_{priceclass}.json"

        table = pandas_df_to_html_table(api_url)
        

        if table :
            return render_template("prices.html", table=table, date=date, priceclass=priceclass)
        else:
            max_date = get_max_date()
            return render_template("price.html", max_date=max_date, error_no_prices="error")
    except ValueError as ve:
        max_date = get_max_date()
        return render_template("prices.html", max_date=max_date, error_no_date=ve)

@app.route("/api", methods=["GET"])
def api_get():
    """function that returns wrongly accessed enpoints. returns you to index"""
    return render_template("index.html")

@app.route("/error")
def show_error():
    return render_template("error.html")

if __name__== "__main__":
    app.run(debug=True)


    


