from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://192.0.0.175:27017/news")

@app.route("/")
def index():
    news = mongo.db.news.find_one()
    return render_template("index.html", news=news)


@app.route("/scrape")
def scrape():
    news = mongo.db.news
    news_data = scraping.scrape_all()
    news.update({}, news_data, upsert=True)
    return "Scraping successful!"


if __name__ == "__main__":
    app.run()
