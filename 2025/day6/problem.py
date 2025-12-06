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
PROBLEM = 6
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2025\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)


def do_op(group, op):
  total = 0 if op == "+" else 1
  for e in group:
    if op == "+":
      total += e
    else:
      total *= e
  return total


def main():
  groups = []
  ops = []
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      if not line:
        continue
      line = list(filter(None, line.rstrip().split(" ")))
      if line[0] == "*" or line[0] == "+":
        ops = line
        break
      line = [int(i) for i in line]
      for i, e in enumerate(line):
        if i >= len(groups):
          groups.append([])
        groups[i].append(e)
  total = 0
  for i, g in enumerate(groups):
    total += do_op(g, ops[i])
  print('part 1:', total)

  grid = []
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = line[:-1]
      if not line:
        continue
      grid.append(list(line))

  total = 0
  op = ""
  group = []

  for x in range(len(grid[0])):
    line = ""
    for g in grid:
      line += g[x]
    if not line.strip():
      total += do_op(group, op.strip())
      group = []
      op = ""
      continue
    op += line[-1]
    group.append(int(line[:-1]))

  total += do_op(group, op.strip())
  print('part 2:', total)


if __name__ == "__main__":
  main()
