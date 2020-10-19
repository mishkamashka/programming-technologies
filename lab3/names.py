from bs4 import BeautifulSoup
import re

def extr_name(filename):
  """
  Вход: nameYYYY.html, Выход: список начинается с года, продолжается имя-ранг в алфавитном порядке.
  '2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' и т.д.
  """
  html = open(filename).read()
  soup = BeautifulSoup(html, features="html.parser")
  
  s = re.search(r"\D+\(d{4}).html", filename).group(1)
  all_names = []
  male_names = []
  female_names = []
  table_rows = re.findall(r"<tr align=\"right\"><td>\d+</td><td>\w+</td><td>\w+</td>", html)
  for row in table_rows:
      m = re.search(r"<tr align=\"right\"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>",row)
      male_names.append([int(m.group(1)), m.group(2)])
      female_names.append([int(m.group(1)), m.group(3)])
  all_names = s + male_names + female_names
  all_names.sort(key = lambda x: x[-1])
  
  names = (all_names, male_names, female_names)
  return names


def main():
  args = sys.argv[1:]
  if not args:
    print 'use: [--file] file [file ...]'
    sys.exit(1)
  elif:
    for filename in args:
      names = extr_name(filename)
      print(filename, "\n", names[0])
      print("TOP-10 male:\n", names[1][:10])
      print("TOP-10 female:\n", names[2][:10])
  
  # для каждого переданного аргументом имени файла, вывести имена  extr_name

  # напечатать ТОП-10 муж и жен имен из всех переданных файлов
 

if __name__ == '__main__':
  main()
