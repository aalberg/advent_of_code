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
PROBLEM = 8
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2025\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
COUNT = 10 if TEST == 1 else 1000

sets = {}
sizes = []


def distance(box1, box2):
  return math.sqrt(sum([(a[0] - a[1])**2 for a in zip(box1, box2)]))


def find(a):
  if sets[a] != a:
    sets[a] = find(sets[a])
    return sets[a]
  return a


def union(a, b):
  ra = find(a)
  rb = find(b)
  if ra == rb:
    return sizes[ra] == len(sets)
  if sizes[ra] < sizes[rb]:
    ra, rb = rb, ra
  sets[rb] = ra
  sizes[ra] += sizes[rb]
  return sizes[ra] == len(sets)


def part1():
  parents = []
  for a, b in sets.items():
    if a == b:
      parents.append(sizes[a])
  total = 1
  for i in sorted(parents, reverse=True)[0:3]:
    total *= i
  print("part 1", total)


def main():
  global sizes
  boxes = []
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      boxes.append(tuple([int(i) for i in line.rstrip().split(",")]))

  dists = []
  for i1, b1 in enumerate(boxes):
    sets[i1] = i1
    for i2, b2 in enumerate(boxes):
      if i2 > i1:
        dists.append((-1 * distance(b1, b2), i1, i2))

  dists = sorted(dists, reverse=True)
  sizes = [1] * len(sets)
  for i, d in enumerate(dists):
    last = d[1], d[2]
    if union(d[1], d[2]):
      break
    if i == COUNT - 1:
      part1()

  print("part 2", boxes[last[0]][0] * boxes[last[1]][0])


if __name__ == "__main__":
  main()
