from app import __version__ as info
from flask import jsonify
from flask_restx import Resource, Api, Namespace
from app.config import Config
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import os

quote_of_day = {}
url = Config.URL

quotes_api = Namespace("quotes", description="Quotes API")

def fetch_quotes(q_url):
    html_doc = requests.get(url)
    soup = BeautifulSoup(html_doc.text, "html.parser")
    quotes_ele = soup.find_all("div", {"class":"grid-item"})
    responses = []
    for quote_ele in quotes_ele:
        temp_dict = {}
        temp_dict["type"] = quote_ele.find("h2", {"class": "qotd-h2"}).text.strip() if quote_ele.find("h2", {"class": "qotd-h2"}) else ""
        temp_dict["quote"] = quote_ele.find("a", {"class": "b-qt"}).text.strip() if quote_ele.find("a", {"class": "b-qt"}) else ""
        temp_dict["author"] = quote_ele.find("a", {"class": "bq-aut"}).get_text() if quote_ele.find("a", {"class": "bq-aut"}) else ""
        responses.append(temp_dict)
    quote_of_day["last_update"] = str(datetime.utcnow())
    quote_of_day["quotes"] = responses

def compare_day():
    if quote_of_day:
        q_date = datetime.fromisoformat(quote_of_day["last_update"])
        t_delta = datetime.utcnow() - q_date
        if t_delta.days >= 1:
            print("Fetching new quotes for the day")
            fetch_quotes(url)
        else:
            print("Using the existing quotes for the day")
    else:
        print("There are no quotes, fetching it...")
        fetch_quotes(url)


@quotes_api.route("")
class BaseResource(Resource):
    def get(self):
        compare_day()
        return jsonify(quote_of_day)