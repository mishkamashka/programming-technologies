import random
from flask import render_template, request
from bs4 import BeautifulSoup
import requests
from guesswho import app, names

correct_name = ""

@app.route("/")
def init():
    return render_template("index.html")

@app.route("/result/", methods=["post"])
def show_result():
    global correct_name
    chosen_name = request.form["options"]
    message = "Wrong!"
    if chosen_name == correct_name:
        message = "You're right"
    return render_template("result.html", message=message)

@app.route("/game/", methods=["post"])
def game():
    global correct_name
    lvl = request.form["options"]

    img_link=""
    options=[]
    if lvl == "easy":
        options = random.sample(names[:10], 4)
        correct_name = random.choice(options)
        img_link = get_random_image_link(correct_name, 30)
    elif lvl = "med":
        options = random.sample(names[:50], 4)
        correct_name = random.choice(options)
        img_link = get_random_image_link(correct_name, 30)
    elif lvl = "hard":
        options = random.sample(names, 4)
        correct_name = random.choice(options)
        img_link = get_random_image_link(correct_name, 30)
    
    return render_template("game.html", img_link=img_link, options=options)

def get_random_image_link(name, n):
    name = name.replace(" ", "%20")
    url = "http://yandex.ru/images/search?text=" + name + "%20face"
    html = requests.get(url).text
    soup = BeautifulSoup(html,"lxml")
    img_links=[]
    for image in soup.find_all("img", {"class": "serp-item__thumb"}, limit=n):
        img_links.append(image["src"])

    return random.choice(img_links)