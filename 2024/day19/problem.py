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
PROBLEM = 19
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def nextline(f):
  line = f.readline()
  if not line:
    return ""
  line = line.rstrip()
  return line


@functools.cache
def can_make_recursive(towels, pattern: str):
  if len(pattern) == 0:
    return 1
  total = 0
  for t in towels:
    if not pattern.startswith(t):
      continue
    total += can_make_recursive(towels, pattern[len(t):])
  return total


def main():
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    towels = tuple(i.strip() for i in nextline(f).split(","))
    _ = nextline(f)
    pattern = "."
    total = 0
    total2 = 0
    while pattern:
      pattern = nextline(f)
      if not pattern:
        break
      total_for_pattern = can_make_recursive(towels, pattern)
      print(f"{pattern} {total_for_pattern}")
      if total_for_pattern:
        total += 1
        total2 += total_for_pattern
    print(f"total: {total} {total2}")


if __name__ == "__main__":
  main()
