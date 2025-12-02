import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time

PART = 2
TEST = 0
PROBLEM = 1
in_dir = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
in_pattern = "test%d.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)
NUMS = "0123456789"


def nextline(f):
  line = f.readline()
  if not line:
    return ""
  line = line.rstrip()
  return line

# def inbounds(x, y):
#   return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

def main():
  with open(in_file, 'r') as f:
    arr1 = []
    arr2 = []
    for line in f:
      line = line.rstrip().split()
      if len(line) == 0:
        continue
      arr1.append(int(line[0]))
      arr2.append(int(line[1]))
    if PART == 1:
      total = 0
      arr1 = sorted(arr1)
      arr2 = sorted(arr2)
      for i in range(len(arr1)):
        total += abs(arr1[i] - arr2[i])
      print(arr1)
      print(arr2)
      print(total)
    else:
      count2 = defaultdict(int)
      for i in arr2:
        count2[i] += 1
      total = 0
      for i in arr1:
        total += i * count2[i]
      # print(arr1)
      # print(arr2)
      print(total)




if __name__=="__main__":
  main()
