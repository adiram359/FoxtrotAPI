import dns
import random
from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)
cluster = MongoClient("mongodb+srv://MrFox:wukme6-Fodfic-boxgan@cluster0.rbtg9.mongodb.net/Foxtrot?retryWrites=true&w=majority")
db = cluster["Foxtrot"]
comics_db = db["comics"]

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/style.css")
def return_style():
    return render_template("style.css")

@app.route("/main.js")
def return_main():
    return render_template("main.js")

@app.route("/random", methods=["GET"])
def get_random_comic():
    x = comics_db.find_one({"_id": random.randint(1, 474)})
    print(x)
    return jsonify(x)


if __name__ == "__main__":
    app.run(debug=True)
