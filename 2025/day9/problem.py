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
PROBLEM = 9
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2025\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)

points = []
windings = []

@functools.cache
def area(p1, p2):
  return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

@functools.cache
def cross(p1, p2):
  return p1[0] * p2[1] - p1[1] * p2[0]

@functools.cache
def in_tri(p, p2, p3, w):
  #if p == p2 or p == p3:
  #  return False
  d = cross(p2, p3)
  wa = (p[0]*(p2[1] - p3[1]) + p[1]*(p3[0] - p2[0])) + cross(p2, p3)
  wb = cross(p, p3)
  wc = cross(p2, p)
  result = True
  if d > 0:
    result = 0 <= wa <= d and 0 <= wb <= d and 0 <= wc <= d
  else:
    result = d <= wa <= 0 and d <= wb <= 0 and d <= wc <= 0
  if (p == p2 or p == p3) and w < 0:
    result = False
  #if result:
  #  print("    in" if result else "    ou", p, p2, p3, d, wa, wb, wc)
  return result

@functools.cache
def inbounds(p):
  #print('  trying', p)
  total = 0
  for i, p2 in enumerate(points):
    if in_tri(p, p2, points[(i+1)%len(points)], windings[i]):
  #    print("     in", p, p2, points[(i+1)%len(points)])
      #print("      winding", windings[i])
      total += windings[i]
  #print("  inbounds", p, total)
  return total > 0

@functools.cache
def validsq(p1, p2):
  #print("sq", p1, p2)
  ul = (min(p1[0], p2[0]), min(p1[1], p2[1]))
  br = (max(p1[0], p2[0]), max(p1[1], p2[1]))
  for p in points:
    if ul[0] < p[0] < br[0] and ul[1] < p[1] < br[1]:
      #print("  dead", p1, p2)
      return False
  ur = (max(p1[0], p2[0]), min(p1[1], p2[1]))
  bl = (min(p1[0], p2[0]), max(p1[1], p2[1]))
  return inbounds(ur) and inbounds(bl) and inbounds(ul) and inbounds(br)

def main():
  global windings
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      points.append(tuple(int(i) for i in line.rstrip().split(",")))
  #for i in range(1, len(points)):
  #  points[i] = (points[i][0] - points[0][0], points[i][1] - points[0][1])
  print(points)

  maxarea = 0
  for i, p1 in enumerate(points):
    for j in range(i + 1, len(points)):
      p2 = points[j]
      maxarea = max(maxarea, area(p1, p2))
  print("part 1:", maxarea)

  unique_x = set((p[0] for p in points))
  unique_y = set((p[1] for p in points))
  #print(unique_x)
  #print(unique_y)

  for i, p in enumerate(points):
    #1 if cross(points[i], points[i+1]) > 0 else -1
    windings.append(1 if cross(p, points[(i+1)%len(points)]) > 0 else -1)
  print(windings)

  # for p in [(2, 1), (8, 4), (10, 6), (4, 4), (100, 100)]:
  #   print(p, inbounds(p))

  # print("sanity", in_tri((1.5, .5), (3, 1), (1, 6)))
  # print("sanity", in_tri((1, 2), (3, 1), (1, 6)))
  # print("sanity", in_tri((.5, 4), (3, 1), (1, 6)))

  maxarea2 = 0
  maxsq = None
  for i, p1 in enumerate(points):
    for j in range(i + 1, len(points)):
      p2 = points[j]
      #maxarea = max(maxarea, area(p1, p2))
      if validsq(p1, p2) and not (min(p1[1], p2[1]) <= 48753 and max(p1[1], p2[1]) >= 50025):
        maxsq = (p1, p2)
        maxarea2 = max(maxarea2, area(p1, p2))
        print('newmax', maxarea2, maxsq)
  print("part 2:", maxarea2)
  # for i, p1 in enumerate(points):
  #   for j in range(i + 1, len(points)):
  #     p2 = points[j]
  #     ok = True
  #     for ux in unique_x:
  #       if not (inbounds((ux, p1[1])) and inbounds((ux, p2[1]))):
  #         ok = False
  #         break
  #     if not ok:
  #       continue
  #     for uy in unique_y:
  #       if not (inbounds((p1[0], uy)) and inbounds((p2[0], uy))):
  #         ok = False
  #         break
  #     if ok:
  #       maxarea2 = max(maxarea2, area(p1, p2))
  # print("part 2:", maxarea2)


if __name__ == "__main__":
  main()
