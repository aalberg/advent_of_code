import bisect
from collections import defaultdict
from collections import deque
import functools
import heapq
import math
import os
import re
import time

PART = 1
TEST = 0
PROBLEM = 3
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2025\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "987654321"
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

grid = []
e = []


def nextline(f):
  line = f.readline()
  if not line:
    return ""
  line = line.rstrip()
  return line


def inbounds(x, y):
  return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def findbiggest(line):
  #print("line", line)
  for n in NUMS:
    #print(line.find(n))
    index = line.find(n)
    #print("  ", n, index)
    if index >= 0:

      return n, index
  print("badbadbabd")
  exit(1)

L = 12
def main():
  total = 0
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.rstrip()
      #print(line)
      #for n in NUMS:
      s = ""
      start = 0
      for j in range(L):

        end = -1 * (L-1) + j
        if end == 0:
          end = len(line)
        #print("range", start, end)
        n, index = findbiggest(line[start:end])
        s += n
        start += index + 1
        #n2, index2 = findbiggest(line[index+1:])
      total += int(s)
      print(s)
      print("")
  print(total)




if __name__ == "__main__":
  main()
