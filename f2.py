from bs4 import BeautifulSoup
import re
html = open("lab3/name2006.html").read()
soup = BeautifulSoup(html, features="html.parser")
# table = soup.find("table")

# print(table,"\n")
output_rows = []
table_rows = re.findall(r"<tr align=\"right\"><td>\d+</td><td>\w+</td><td>\w+</td>", html)
for row in table_rows:
    m = re.search(r"<tr align=\"right\"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>",row)
    output_rows.append(m.group(1))
    output_rows.append(m.group(2))


print(output_rows)