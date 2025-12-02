import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time
import re

PART = 2
TEST = 0
PROBLEM = 3
in_dir = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
in_pattern = "test%d.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)
NUMS = "0123456789"


def main():
  with open(in_file, 'r') as f:
    total = 0
    enabled = True
    for line in f:
      line = line.rstrip()
      if PART == 1:
        a = re.findall("mul\((\d+),(\d+)\)", line)
        print(a)
        for b in a:
          print(b)
          total += int(b[0]) * int(b[1])
        print(total)
      else:
        for a in re.finditer("(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))", line):
          #print(a)
          if a.group(0).startswith("mul"):
            print("mul", int(a.group(2)), int(a.group(3)))
            if enabled:
              total += int(a.group(2)) * int(a.group(3))
          elif a.group(0).startswith("don't"):
            enabled = False
            print("disable")
          elif a.group(0).startswith("do"):
            enabled = True
            print("enable")
        print(total)


if __name__ == "__main__":
  main()
