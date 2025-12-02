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
PROBLEM = 1
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2025\\day{PROBLEM}"
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


def sign(i):
  if i < 0:
    return -1
  elif i > 0:
    return 1
  return 0


def main():
  cur = 50
  z = 0
  print("0 0 0 50")
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.rstrip()
      d = 1 if line[0] == "R" else -1
      m = int(line[1:]) * d
      t = abs(m) // 100
      old = cur
      cur += m
      cur = cur % 100
      if cur == 0:
        z += 1
      elif old != 0:
        if d == 1 and old > cur:
          z += 1
        elif d == -1 and old < cur:
          z += 1
      z += t
  print("--------")
  print(z)


if __name__ == "__main__":
  main()
