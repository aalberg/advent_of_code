import os
import itertools

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2022\\"
in_file = os.path.join(in_dir, "input3.txt")

prios = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def toPrio(s):
  return prios.find(s) + 1

def findCommon(a, b):
  m = {}
  for ca in a:
    m[ca] = True
  for cb in b:
    if cb in m.keys():
      return cb

def findCommon2(a, b, c):
  print(a, b, c)
  m = {}
  for ca in a:
    if ca not in m:
      m[ca] = 1
  for cb in b:
    if cb in m.keys():
      m[cb] += 1
  for cc in c:
    if cc in m.keys():
      print("m", cc, m[cc])
    if cc in m.keys() and m[cc] >= 2:
      return cc

def main():
  with open(in_file, 'r') as f:
    score = 0
    # for line in f:
    #   line = line.rstrip()
    #   if len(line) == 0:
    #     continue
    #   elif len(line) % 2 == 1:
    #     print("BAD", line)
    #     continue

    #   d = int(len(line)/2)
    #   a = line[0:d]
    #   b = line[d:]

    line_set = ["", "", ""]
    for i, line in enumerate(f):
      line = line.rstrip()
      line_set[i % 3] = line
      if i % 3 != 2:
        continue
      print(line_set)


      z = findCommon2(line_set[0], line_set[1], line_set[2])
      print("z:", z)
      s = toPrio(z)
      print(score, s, z)
      score += s

    print(score)

if __name__=="__main__":
  main()