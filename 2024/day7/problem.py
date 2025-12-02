import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import re
import time

PART = 1
TEST = 1
PROBLEM = 8
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"

def search(cur, nums, target):
  if len(nums) == 0:
    return cur == target
  return search(cur + nums[0], nums[1:], target) or search(
      cur * nums[0], nums[1:], target)

def search2(cur, nums, target):
  if len(nums) == 0:
    return cur == target
  return search2(cur + nums[0], nums[1:], target) or search2(
      cur * nums[0], nums[1:], target) or search2(
          int(str(cur) + str(nums[0])), nums[1:], target)


def main():
  total = 0
  total2 = 0
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.rstrip().split(" ")
      line[0] = line[0][:-1]
      line = [int(i) for i in line]
      target = line[0]
      nums = line[1:]
      if search(nums[0], nums[1:], target):
        total += target
      if search2(nums[0], nums[1:], target):
        total2 += target
  print(total)
  print(total2)


if __name__ == "__main__":
  main()
