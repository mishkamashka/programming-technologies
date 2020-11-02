import random
import sys
import os
import re

def mem_dict(filename):
  dictionary = {}
  file = open(filename)
  for line in file:
    prev_word = ""
    regex = re.compile('[^a-zA-Z]$')
    for bare_word in line.lower().split(' '):
      word = regex.sub('', bare_word)
      if prev_word == "" or word == "":
        prev_word = word
        continue
      if prev_word not in dictionary:
        dictionary[prev_word] = [word]
      else:
        dictionary[prev_word].append(word)
      prev_word = word
  return dictionary

def generate_text(words_count, dictionary):
  keys = list(dictionary.keys())
  prev_word = random.choice(keys) 
  text = [prev_word]
  for i in range(0, words_count-1):
    if prev_word not in dictionary:
      return text       # if there're no following words then that's it
    new_word = random.choice(dictionary[prev_word])
    text.append(new_word)
    prev_word = new_word
  return text

def main():
  args = sys.argv[1:]
  if not args:
    print("use: [--file] file")
    sys.exit(1)
  filename = args[0]
  if not(os.access(filename, os.R_OK)):
    print("File does not exist or cannot be read.")
    sys.exit(1)
  print(*generate_text(5, mem_dict(filename)))

if __name__ == '__main__':
  main()
