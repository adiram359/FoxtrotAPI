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
    """
        Scrapes comic from url and puts it in database
    """
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
        date = parse_date(entry.find(class_="entry-summary").get_text())

        comic = {
            "_id": id,
            "author": "Bill Amend",
            "title": title,
            "img_src": img_src,
            "date": date
        }
        result_id = comics_db.insert_one(comic)
        print("Succes: {}:".format(result_id))
        id += 1

def parse_date(date):
    """
        Parses string in the from:
        "Published Month Day, Year" -> "Month.Day.Year"
    """

    print(date)
    date = date.replace(",", "")
    list = date.split()
    list.pop(0)
    dict = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    assert list[0] in dict
    assert list[1].isnumeric()
    assert list[2].isnumeric()
    return ("{}.{}.{}".format(dict[list[0]], list[1], list[2]))
for i in range(1, 80):
    get("https://foxtrot.com/page/{}".format(i))
