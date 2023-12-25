import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time

PART = 1
TEST = 1
PROBLEM = 16
in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_pattern = "test%d.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)
NUMS = "0123456789"

grid = []
e = []

def nextline(f):
  line = f.readline()
  if not line:
    return ""
  line = line.rstrip()
  return line

def inbounds(x, y):
  return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

def main():
  with open(in_file, 'r') as f:
    for line in f:
      line = line.rstrip()
      grid.append(line)
      e.append([0] * len(line))
  for l in grid:
    print(l)
  for l in e:
    print(l)



if __name__=="__main__":
  main()
