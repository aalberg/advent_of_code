import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import re
import time

PART = 2
TEST = 0
PROBLEM = 13
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def nextline(f):
  line = f.readline()
  if not line:
    return ""
  line = line.rstrip()
  return line

def invert(a, b, c, d):
  det = a * d - (b * c)
  if det == 0:
    return None
  r = [d, -1*b, -1*c, a]
  return r, det

def solve(a, b, t):
  i, det = invert(a[0], b[0], a[1], b[1])
  if not i:
    return None, None
  x = i[0]*t[0] + i[1]*t[1]
  y = i[2]*t[0] + i[3]*t[1]
  if (x % det) == 0 and  (y % det) == 0:
    return x//det, y//det
  return None, None

def main():
  total = 0
  total2 = 0
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    while True:
      a = nextline(f)
      if a == "":
        break
      b = nextline(f)
      t = nextline(f)
      _ = nextline(f)

      a = [int(p.split("+")[1]) for p in a[10:].split(",")]
      b = [int(p.split("+")[1]) for p in b[10:].split(",")]
      t = [int(p.split("=")[1]) for p in t[7:].split(",")]

      # part 1
      x, y = solve(a, b, t)
      if x and x < 100 and y and y < 100:
        total += 3*x + y

      # part 2
      for i in range(2):
        t[i] += 10000000000000
        x, y = solve(a, b, t)
      if x and y:
        total2 += 3*x + y
  print(total)
  print(total2)


if __name__ == "__main__":
  main()
