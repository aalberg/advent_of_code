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
TEST = 1
PROBLEM = 11
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2025\\day{PROBLEM}"
IN_PATTERN = "test2.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)

parents = defaultdict(set)

@functools.cache
def num_paths(node, target):
  if node == target:
    return 1
  return sum(num_paths(p, target) for p in parents[node])


def main():
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.rstrip().split(": ")
      for child in line[1].split():
        parents[child].add(line[0])
  print("part 1:", num_paths("out", "you"))
  print("part 2:", (num_paths("out", "fft") * num_paths("fft", "dac") *
                    num_paths("dac", "svr")) +
        (num_paths("out", "dac") * num_paths("dac", "fft") *
         num_paths("fft", "svr")))


if __name__ == "__main__":
  main()
