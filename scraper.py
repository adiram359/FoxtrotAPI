import dns
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://MrFox:wukme6-Fodfic-boxgan@cluster0.rbtg9.mongodb.net/Foxtrot?retryWrites=true&w=majority")
db = cluster["Foxtrot"]
comics_db = db["comics"]
id = 0

FOXTROT = "https://foxtrot.com/"

def get(page):
    req = Request(page, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'lxml')
    cartoon_set = soup.find_all('article')

    global id
    for cartoon in cartoon_set:
        link = cartoon.find(class_="entry").find('a').get('href')
        req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, 'lxml')
        entry = soup.find(class_="entry")
        title = entry.find(class_="entry-newtitle").get_text()
        img_src = entry.find(class_="entry-content").find("img").get('src')

        comic = {
            "_id": id,
            "author": "Bill Amend",
            "title": title,
            "img_src": img_src
        }
        result_id = comics_db.insert_one(comic)
        print("Succes: {}:".format(result_id))
        id += 1



print(comics_db.find_one({"_id": 65}))
