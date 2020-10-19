def num_of_items(count):
  number = str(count)
  if count >= 10:
    number = "many"
  return "Number of: " + number
  
def start_end_symbols(s):
  if len(s) < 2:
    return "The string is too short"
  return s[0:2] + s[-2:]

def replace_char(s):
  return s[0] + s[1:].replace(s[0], '*')

def str_mix(a, b):
  return b[0:2] + a[2:] + " " + a[0:2] + b[2:]

def test(res, expt):
  return "Expected result: " + expt + "\nResult: " + res + "\n\n"
  
def main():

  print test(start_end_symbols('welcome'), 'weme')

  print test(replace_char('bibble'), 'bi**le')

  print test(num_of_items(5), 'Number of: 5')

  print test(num_of_items(23), 'Number of: many')

  print test(str_mix('max', 'pid'), 'pix mad')

if __name__ == '__main__':
  main()

