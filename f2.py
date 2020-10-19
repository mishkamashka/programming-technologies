from bs4 import BeautifulSoup
import re
filename = "lab3/name2006.html"
html = open(filename).read()
soup = BeautifulSoup(html, features="html.parser")
  
s = re.search(r"\D+(\d{4}).html", filename).group(1)
all_names = []
male_names = []
female_names = []
table_rows = re.findall(r"<tr align=\"right\"><td>\d+</td><td>\w+</td><td>\w+</td>", html)
for row in table_rows:
    m = re.search(r"<tr align=\"right\"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>",row)
    male_names.append([m.group(2), int(m.group(1))])
    female_names.append([m.group(3), int(m.group(1))])
all_names = [s] + male_names + female_names
all_names.sort(key = lambda x: x[0])


print(all_names[:10])