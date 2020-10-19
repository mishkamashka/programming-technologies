

def rm_adj(nums):
  return list(set(nums))


def merge(lst1, lst2):
  return sorted(lst1 + lst2)

def test(res, expt):
  return "Expected result: " + str(expt) + "\nResult: " + str(res) + "\n\n"
  
def main():

  print test(rm_adj([0, 2, 2, 3]), [0, 2, 3])

  print test(merge([0, 4, 6, 7], [1, 2, 5, 8]), [0,1, 2, 4, 5, 6, 7, 8])

if __name__ == '__main__':
  main()
