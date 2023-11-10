import pytest
import urllib.request
import ssl
import requests

context = ssl._create_unverified_context()

def test_index():
    assert urllib.request.urlopen("http://127.0.0.1:5000/", context=context, timeout=10)

def test_prices():
    """This doesn't show up but it is rendered in api_post"""
    assert urllib.request.urlopen("http://127.0.0.1:5000/prices", context=context, timeout=10)