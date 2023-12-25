import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time

PART = 2
TEST = 0
PROBLEM = 12
in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_pattern = "test%d.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)

springs = ""
nums = []
visited = {}

def can_fit(si, num):
  #print("can_fit", si, num)
  if si > 0 and springs[si - 1] == "#":
    return False
  if si + num < len(springs) and springs[si + num] == "#":
    return False
  for i in range(num):
    si2 = si + i
    if springs[si2] == ".":
      return False
  return True

def place_elements(si, ni, cur=[]):
  #print(si, ni)
  if (ni, si) in visited:
    return visited[(ni, si)]
  if ni == len(nums):
    for i in range(si, len(springs)):
      if springs[i] == "#":
        return 0
    #print(cur)
    return 1
  if si >= len(springs):
    return 0
  num = nums[ni]
  max_index = len(springs) - (sum(nums[ni:]) + len(nums[ni:]) - 1)
  next_spring = springs[si:].find("#")
  if next_spring >= 0:
    max_index = min(max_index, next_spring + si)
  total = 0
  for i in range(si, max_index + 1):
    if can_fit(i, num):
      total += place_elements(i + num + 1, ni + 1, cur + [i])
  visited[(ni, si)] = total
  return total

def main():
  global springs
  global nums
  global visited
  total = 0
  with open(in_file, 'r') as f:
    for line in f:
      springs, nums = line.rstrip().split()
      if PART == 2:
        springs = "?".join([springs for i in range(5)])
        nums = ",".join([nums for i in range(5)])
      nums = [int(n) for n in nums.split(",")]
      visited = {}
      print(springs, nums)
      count = place_elements(0, 0)
      total += count
      print("count", count)
  print("total", total)


if __name__=="__main__":
  main()
