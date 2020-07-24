import re
import dns
import random
import requests
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
cluster = MongoClient("mongodb+srv://MrFox:wukme6-Fodfic-boxgan@cluster0.rbtg9.mongodb.net/Foxtrot?retryWrites=true&w=majority")
db = cluster["Foxtrot"]
comics_db = db["comics"]

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/title/<title>")
def print_man(title):
    title = " ".join(title.split("."))
    x = comics_db.find_one({"title": " ".join(title.split("."))})
    return render_template("index.html")


@app.route("/random", methods=["GET"])
def get_random_comic():
    x = comics_db.find_one({"_id": random.randint(1, 474)})
    return jsonify(x)


if __name__ == "__main__":
    app.run(debug=True)
