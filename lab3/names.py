import re
import sys
import os

def extr_name(filename):
  if not(os.access(filename, os.R_OK)):
    print("File does not exist or cannot be read.")
    sys.exit(1)
  html = open(filename).read()
  
  all_names = []
  male_names = []
  female_names = []
  table_rows = re.findall(r"<tr align=\"right\"><td>\d+</td><td>\w+</td><td>\w+</td>", html)
  for row in table_rows:
      m = re.search(r"<tr align=\"right\"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>",row)
      male_names.append([int(m.group(1)), m.group(2)])
      female_names.append([int(m.group(1)), m.group(3)])
  all_names = male_names + female_names
  all_names.sort(key = lambda x: x[-1])
  
  names = (all_names, male_names, female_names)
  return names

def names_to_str(filename, names):
  s = filename + "\n"
  for name in names:
    s += str(name[0]) + " " + name[1] + "\n"
  return s


def main():
  args = sys.argv[1:]
  if not args:
    print("use: [--file] file [file ...]")
    sys.exit(1)
  else:
    for filename in args:
      s = re.search(r"\D+(\d{4}).html", filename).group(1)

      names = extr_name(filename)
      print(names_to_str(s, names[0]))
      print(names_to_str("TOP-10 male:", names[1][:10]))
      print(names_to_str("TOP-10 female:", names[2][:10]))

if __name__ == '__main__':
  main()
