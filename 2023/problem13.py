import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time

PART = 1
TEST = 0
PROBLEM = 13
in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_pattern = "test%d.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)
NUMS = "0123456789"

grid = []
overall = 0

def find_reflections(dim_to_search):
  x_max = len(grid[0])
  y_max = len(grid)
  outer_max = x_max if dim_to_search == 0 else y_max
  inner_max = y_max if dim_to_search == 0 else x_max

  total = 0
  total2 = 0
  for o in range(0, outer_max - 1):
    total_wrong = 0
    for d in range(0, min(o + 1, outer_max - 1 - o)):
      #print(dim_to_search, o, d, o1, o2)
      for i in range(0, inner_max):
        if dim_to_search == 0:
          if grid[i][o - d] != grid[i][o + 1 + d]:
            total_wrong += 1
        elif dim_to_search == 1:
          if grid[o - d][i] != grid[o + 1 + d][i]:
            total_wrong += 1
    if total_wrong == 0:
      total += o + 1
    elif total_wrong == 1:
      total2 += o + 1
  return total, total2

def do_problem2():
  tx, tx2 = find_reflections(0)
  ty, ty2 = find_reflections(1)
  return (tx + 100 * ty, tx2 + 100 * ty2)

def main():
  global grid
  overall = 0
  overall2 = 0
  with open(in_file, 'r') as f:
    for line in f:
      line = line.rstrip()
      
      if len(line) == 0:
        t1, t2 = do_problem2()
        overall += t1
        overall2 += t2
        grid = []
      else:
        grid.append(line)
  t1, t2 = do_problem2()
  overall += t1
  overall2 += t2
  print("overall", overall)
  print("overall2", overall2)

if __name__=="__main__":
  main()
