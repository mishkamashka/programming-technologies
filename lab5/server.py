import random
from flask import Flask
from flask import render_template
from random import shuffle
import requests
import re

entry_point = Flask(__name__, static_url_path='/static')


def read_names_from_file(filename):
    f = open(filename, 'r')
    data = f.read()
    return list(map(lambda x: x.split('(')[0].strip(), data.splitlines()))


names = read_names_from_file("names.txt")
picture_urls = dict()


def get_urls(name):
    if name not in picture_urls.keys():
        picture_urls[name] = get_links(name)
    return picture_urls[name]


def get_random_name(lower_bound):
    idx = random.randint(0, lower_bound)
    entry = names[idx]
    return entry


@entry_point.route("/")
def hello():
    return render_template('index.html')


@entry_point.route("/start/<level_param>")
def game(level_param="low"):
    level_param = switch_level_to_int(level_param)
    idx_to_guess = random.randint(0, level_param)
    name_options = names[:level_param]
    shuffle(name_options)
    image_links = get_urls(names[idx_to_guess])[:3]
    shuffle(image_links)
    return render_template('game.html',
                           difficulty="1-" + str(level_param + 1) + " names",
                           names=name_options,
                           name_index=idx_to_guess,
                           image_links=image_links)


@entry_point.route("/guess/<id>/<name>")
def guess(id="-1", name=""):
    id = int(id)
    if id == -1:
        return "invalid request"
    if names[id] == name:
        return "True"
    return "False"


def switch_level_to_int(argument):
    switcher = {
        "low": 9,
        "medium": 49,
        "high": 99,
    }
    return switcher.get(argument, "invalid level")


def get_links(name):
    url = 'https://www.google.com/search?q=' + name + '&client=firefox-b-ab&tbm=isch&tbo=u&source=univ&sa=X&ved=2ahUKEwjN5fWwxu3eAhUQmIsKHeA-D90QsAR6BAgEEAE'
    headers = {
        'User-Agent': 'Nokia5250/10.0.011 (SymbianOS/9.4; U; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Safari/525 3gpp-gba'}
    response = requests.get(url, headers=headers)
    text_file = open("output.html", "w", encoding='utf-8')
    text_file.write(response.text)
    text_file.close()
    ans = []
    results = re.findall(r'<img src="h.*?>', response.text)
    for result in results:
        urlg = re.search(r'"(.+?)"', result)
        if urlg:
            url = urlg.group(1)
            ans.append(url)
    return ans


if __name__ == '__main__':
    entry_point.run(debug=True)