from application import app
import urllib

def test_json_data():
    api_url = "https://www.elprisetjustnu.se/api/v1/prices/2023/05-05_SE1.json"
    df = app.json_data_to_pandas_df(api_url)
    assert len(df) > 0

def test_to_html():
    api_url = "https://www.elprisetjustnu.se/api/v1/prices/2023/05-05_SE1.json"
    html_table = app.pandas_df_to_html_table(api_url)
    
    assert len(html_table) > 0
    
def test_date():
    max_date = app.get_max_date()
    assert len(max_date) == 10
