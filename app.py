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
    """
        default landing page
    """
    return render_template("index.html")

def query_db(filter):
    """
    queries the database and retuns a JSON:
    {
        _id: id of comic,
        author: "Bill Amend",
        title: comic title,
        img_src: img.png,
        date: Month.Date.Year,
        success: True if in db else false
    }
    """
    query_result = comics_db.find_one(filter)
    print(query_result)
    if query_result == None:
        return jsonify({
        "success": False
        })
    else:
        query_result["success"] = True
        return jsonify(query_result)

@app.route("/title/<title>")
def get_by_title(title):
    """
        Returns comic based on title
    """
    filter = {"title": " ".join(title.split("."))}
    return query_db(filter)

@app.route("/random", methods=["GET"])
def get_random_comic():
    """
        Returns a random comic
    """
    filter = {"_id": random.randint(1, 474)}
    return query_db(filter)

@app.route("/date/<date>")
def get_by_date(date):
    """
        Returns comic by date published
    """
    lst = date.split(".")
    for i in range(len(lst)):
        if lst[i][0] == "0":
            lst[i] = lst[i][1:]
    date = ".".join(lst)
    filter = {"date": date}
    return query_db(filter)


if __name__ == "__main__":
    app.run(debug=True)
