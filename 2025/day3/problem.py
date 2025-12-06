import bisect
from collections import defaultdict
from collections import deque
import functools
import heapq
import math
import os
import re
import time

PART = 2
TEST = 0
PROBLEM = 3
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2025\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "987654321"
L = 12 if PART == 2 else 2


def findbiggest(line):
  for n in NUMS:
    index = line.find(n)
    if index >= 0:
      return n, index
  print("badbadbad")
  exit(1)


def main():
  total = 0
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.rstrip()
      s = ""
      start = 0
      for j in range(L):
        end = -1 * (L - 1) + j
        if end == 0:
          end = len(line)
        n, index = findbiggest(line[start:end])
        s += n
        start += index + 1
      total += int(s)
  print(total)


if __name__ == "__main__":
  main()
