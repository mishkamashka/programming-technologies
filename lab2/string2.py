import re

def v(s):
  if len(s) > 3 and s[-3:] != 'ing':
    s += 'ing'
  elif len(s) > 3:
    s += 'ly'
  return s


def nb(s):
  return re.sub(r'\bnot\b.*\bbad\b', 'good', s)

def test(res, expt):
  return "Expected result: " + str(expt) + "\nResult: " + str(res) + "\n\n"
  
def main():

  print test(v("call"), "calling")
  print test(v("ap"), "ap")
  print test(v("willing"), "willingly")

  print test(nb('This music is not so bad!'), 'This music is good!')

if __name__ == '__main__':
  main()
