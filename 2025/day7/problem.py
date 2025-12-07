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
PROBLEM = 7
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2025\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)


def main():
  grid = []
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.rstrip()
      grid.append(line)

  active = defaultdict(int)
  active[grid[0].find("S")] = 1
  total = 0
  for row in grid:
    new_active = defaultdict(int)
    for a, count in active.items():
      if row[a] == "^":
        total += 1
        new_active[a - 1] += count
        new_active[a + 1] += count
      else:
        new_active[a] += count
    active = new_active

  print("part 1:", total)
  print("part 2:", sum(active.values()))


if __name__ == "__main__":
  main()
