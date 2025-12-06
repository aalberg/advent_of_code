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
PROBLEM = 5
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2025\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)


def nextline(f):
  line = f.readline()
  if not line:
    return ""
  line = line.rstrip()
  return line


def intersects(s1, e1, s2, e2):
  return ((s2 <= e1 and e2 >= e1) or (s2 <= s1 and e2 >= s1) or
          (s1 <= e2 and e1 >= e2) or (s1 <= s2 and e1 >= s2))


def mergerange(s1, e1, s2, e2):
  return [min(s1, s2), max(e1, e2)]


def main():
  ranges = []

  with open(IN_FILE, 'r', encoding='utf-8') as f:
    while True:
      line = nextline(f)
      if not line:
        break
      r = [int(i) for i in line.split("-")]
      r[1] += 1

      merged = True
      while merged:
        merged = False
        for i, old_r in enumerate(ranges):
          if intersects(old_r[0], old_r[1], r[0], r[1]):
            r = mergerange(old_r[0], old_r[1], r[0], r[1])
            merged = True
            del ranges[i]
            break
      ranges.append(r)

    total2 = 0
    for r in sorted(ranges):
      total2 += r[1] - r[0]

    total = 0
    while True:
      line = nextline(f)
      if not line:
        break
      i = int(line)
      for r in ranges:
        if r[0] <= i and r[1] > i:
          total += 1
          break
    print("part 1", total)
    print("part 2", total2)


if __name__ == "__main__":
  main()
