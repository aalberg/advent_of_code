import os
import ast
import functools

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2022\\"
in_file = os.path.join(in_dir, "input13.txt")

def nextline(f):
  line = f.readline()
  if not line:
    #print("DONE")
    return -1
  line = line.rstrip()
  #print(line)
  return line

def cmp(a, b):
  return (a > b) - (a < b) 

def compare(a, b, d=0):
  #print("  " * d, a, b)
  if type(a) == int and type(b) == int:
    return cmp(a, b)
  elif type(a) == list and type(b) == list:
    if len(a) == 0 and len(b) != 0:
      return -1
    elif len(a) != 0 and len(b) == 0:
      return 1
    for i in range(max(len(a), len(b))):
      if i >= len(a):
        return -1
      elif i >= len(b):
        return 1
      temp = compare(a[i], b[i], d + 1)
      if temp != 0:
        return temp
  elif type(a) == list and type(b) == int:
    return compare(a, [b], d + 1)
  elif type(a) == int and type(b) == list:
    return compare([a], b, d + 1)
  else:
    #print("BAD", a, b)
    return 100000
  return 0

def main():
  with open(in_file, 'r') as f:
    # pairset = 1
    # total = 0
    # while True:
    #   a = ast.literal_eval(nextline(f).rstrip())
    #   b = ast.literal_eval(nextline(f).rstrip())
    #   print(a)
    #   print(b)
    #   result = compare(a, b, 0)
    #   print(pairset, result == -1, result)
    #   if result == -1:
    #     total += pairset
    #   print("")

    #   newline = nextline(f)
    #   pairset += 1
    #   if newline == -1:
    #     break

    # print(total)
    lists = [[[2]], [[6]]]
    for line in f:
      line = line.rstrip()
      if len(line) == 0:
        continue
      lists.append(ast.literal_eval(line))
    lists.sort(key=functools.cmp_to_key(compare))
    for l in lists:
      print(l)
    i2 = lists.index([[2]]) + 1
    i6 = lists.index([[6]]) + 1
    print(i2, i6, i2 * i6)
    #print(lists)

if __name__=="__main__":
  main()
