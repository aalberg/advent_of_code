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
PROBLEM = 5
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"

mapping = defaultdict(set)

def nextline(f):
  line = f.readline()
  if not line:
    return ""
  line = line.rstrip()
  return line


def insert_sort(nums):
  s = [nums[0]]
  for n in nums[1:]:
    print(s)
    inserted = False
    for i in range(len(s)):
      if s[i] in mapping[n]:
        s.insert(i, n)
        inserted = True
        break
    if not inserted:
      s.append(n)
  print(s)
  return s



def main():
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    while True:
      line = nextline(f)
      if len(line) == 0:
        break
      line = [int(i) for i in line.split("|")]
      mapping[line[0]].add(line[1])

    total = 0
    total2 = 0
    while True:
      line = nextline(f)
      if len(line) == 0:
        break

      line = [int(i) for i in line.split(",")]
      seen = set()
      ok = True
      for i in line:
        for s in seen:
          if s in mapping[i]:
            print(i, s)
            ok = False
            break
        if not ok:
          break
        seen.add(i)
      print("----------")
      print(line)
      if ok:
        total += line[int(len(line) / 2)]
      else:
        s = insert_sort(line)
        total2 += s[int(len(s) / 2)]
      print(ok)
    print(total)
    print(total2)


if __name__ == "__main__":
  main()
