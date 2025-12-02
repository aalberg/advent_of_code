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
PROBLEM = 22
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def mix(num, secret):
  return num ^ secret


def prune(secret):
  return secret % 16777216


def nextnum(secret):
  secret = prune(mix(secret * 64, secret))
  secret = prune(mix(secret // 32, secret))
  secret = prune(mix(secret * 2048, secret))
  return secret


def main():
  seq_values = defaultdict(int)
  total = 0
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      secret = int(line.rstrip())
      deltas = deque()
      delta_seq_values = {}
      for _ in range(2000-4):
        next_secret = nextnum(secret)
        deltas.append((next_secret % 10) - (secret % 10))
        if len(deltas) > 4:
          deltas.popleft()
        secret = next_secret

        if len(deltas) == 4 and tuple(deltas) not in delta_seq_values:
          delta_seq_values[tuple(deltas)] = secret % 10
      total += secret
      for k, v in delta_seq_values.items():
        seq_values[k] += v
  print("total ", total)
  print("max ", max(seq_values.values()))


if __name__ == "__main__":
  main()
