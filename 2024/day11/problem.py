import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import re
import time

PART = 1
TEST = 0
PROBLEM = 11
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"
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


def do_step(stones):
  new_stones = defaultdict(int)
  for i, count in stones.items():
    if i == 0:
      new_stones[1] += count
      continue
    str_i = str(i)
    if len(str_i) % 2 == 0:
      l = int(len(str_i) / 2)
      new_stones[int(str_i[:l])] += count
      new_stones[int(str_i[l:])] += count
    else:
      new_stones[i * 2024] += count
  return new_stones


def main():
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      stones = defaultdict(int)
      for i in [int(i) for i in line.rstrip().split()]:
        stones[i] += 1
      for i in range(75):
        if i == 25:
          print("part 1 ", sum(stones.values()))
        stones = do_step(stones)
      print("part 2 ", sum(stones.values()))


if __name__ == "__main__":
  main()
