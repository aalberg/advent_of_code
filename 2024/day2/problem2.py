import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time

PART = 1
TEST = 0
PROBLEM = 2
in_dir = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
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
    count = 0
    for line in f:
      line = line.rstrip().split()
      line = [int(i) for i in line]
      # safe = True
      # inc = line[0] < line[1]
      # for i in range(len(line) - 1):
      #   diff = abs(line[i] - line[i+1])
      #   if diff == 0 or diff >= 4:
      #     #print("diff")
      #     safe = False
      #     break
      #   if inc and line[i] >= line[i+1]:
      #     #print("inc")
      #     safe = False
      #     break
      #   if not inc and line[i] <= line[i+1]:
      #     #print("not inc")
      #     safe = False
      #     break

      # print("line", line)
      for skip in range(len(line)):
        safe = True
        line2 = []
        if skip == 0:
          line2 = list(line[1:])
        elif skip == len(line) - 1:
          line2 = list(line[:-1])
        else:
          line2 = list(line[:skip] + line[skip+1:])
        # print("line2", line2)
        inc = line2[0] < line2[1]
        for i in range(len(line2) - 1):
          diff = abs(line2[i] - line2[i+1])
          if diff == 0 or diff >= 4:
            # print("diff")
            safe = False
            break
          if inc and line2[i] >= line2[i+1]:
            # print("inc")
            safe = False
            break
          if not inc and line2[i] <= line2[i+1]:
            # print("not inc")
            safe = False
            break
        if safe:
          break

      if TEST == 1:
        print(line, safe)
      if safe:
        count += 1
    print(count)



if __name__=="__main__":
  main()
