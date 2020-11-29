from flask import Flask
import random
from flask import render_template, request
from bs4 import BeautifulSoup
import requests
import re

app = Flask(__name__)

names = []

correct_name = ""

lvl=""

@app.route("/")
def init():
    return render_template("index.html")

@app.route("/result", methods=["post"])
def show_result():
    global correct_name
    chosen_name = request.form["options"]
    message = "Nope, it's " + correct_name
    if chosen_name == correct_name:
        message = "Yep, that is " + correct_name
    return render_template("result.html", message=message, lvl=lvl)

@app.route("/game", methods=["post"])
def game():
    global correct_name
    global lvl
    lvl = request.form["options"]
    print(lvl)
    img_link=""
    options=[]
    if lvl == "easy":
        options = random.sample(names[:10], 4)
        correct_name = random.choice(options)
        img_link = get_random_image_link(correct_name, 30)
    elif lvl == "med":
        options = random.sample(names[:50], 4)
        correct_name = random.choice(options)
        img_link = get_random_image_link(correct_name, 30)
    elif lvl == "hard":
        options = random.sample(names, 4)
        correct_name = random.choice(options)
        img_link = get_random_image_link(correct_name, 30)
    return render_template("game.html", img_link=img_link, options=options)

def get_random_image_link(name, n):
  query="%2B".join(name.split())
  url = "https://www.google.com/search?q=" + query + "&tbm=isch&tbs=isz:lt,islt:6mp"
  response = requests.get(url).text
  soup = BeautifulSoup(response,"html.parser")
  img_links = [a["src"] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})]
  return random.choice(img_links)

    # name = name.replace(" ", "%20")
    # url = "http://yandex.ru/images/search?text=" + name + "%20face"
    # html = requests.get(url).text
    # soup = BeautifulSoup(html,"lxml")
    # img_links=[]
    # for image in soup.find_all("img", {"class": "serp-item__thumb"}, limit=n):
    #     img_links.append(image["src"])

    # return random.choice(img_links)

def upload_names():
  f = open('names.txt', 'r')
  for name in f:
    names.append(name[:-1])

if __name__ == '__main__':
  upload_names()
  app.run()