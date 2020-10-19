def me(words):
  count = 0
  for word in words:
    if len(word) > 2 and word[0] == word[-1]:
      count += 1
  return count


def fx(words):
  words.sort()
  xwords = []
  for i in range(len(words) - 1, -1, -1):
    if words[i].startswith('x'):
        xwords.insert(0, words[i])
        words.remove(words[i])
  return xwords + words


def cs(lst):
  lst.sort(key = lambda x: (x[-1]))
  return lst

def test(res, expt):
  return "Expected result: " + str(expt) + "\nResult: " + str(res) + "\n\n"
  
def main():

  print test(me(['welcome', 'heh', 'aa', 'aama']), 2)

  print test(fx(['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc']), ['xacadu', 'xyz', 'aabbbccc', 'apple', 'tix'])

  print test(cs([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
  main()
