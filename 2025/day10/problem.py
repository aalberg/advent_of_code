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
PROBLEM = 10
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2025\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

grid = []
e = []


def nextline(f):
  line = f.readline()
  if not line:
    return ""
  line = line.rstrip()
  return line


def inbounds(x, y):
  return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def toggle(curlights, button):
  newlights = list(curlights)
  #print(newlights)
  for b in button:
    newlights[b] = not newlights[b]
  return tuple(newlights)

def bfs(target, buttons):
  #print('bfs', target, buttons)
  q = deque()
  q.append((tuple([False] * len(target)), 0))
  v = set()
  v.add(tuple([False] * len(target)))

  while q:
    lights, d = q.popleft()

    for b in buttons:
      nextlights = toggle(lights, b)
      if nextlights == target:
        #print("done", d + 1)
        return d + 1
      if nextlights not in v:
        q.append((nextlights, d + 1))
        v.add(nextlights)
        #print(" " * d, nextlights)

def increment(curlights, button):
  newlights = list(curlights)
  #print(newlights)
  for b in button:
    newlights[b] += 1
  return tuple(newlights)

def bfs2(target, buttons):
  #print('bfs2', target, buttons)
  q = deque()
  q.append((tuple([0] * len(target)), 0, 0))
  v = set()
  v.add(tuple([0] * len(target)))

  while q:
    lights, d, fb = q.popleft()
    print(" " * d, lights, d, fb)

    for i, b in enumerate(buttons[fb:]):
      nextlights = increment(lights, b)
      if nextlights == target:
        #print("done", d + 1)
        return d + 1
      ok = True
      for a, b, in zip(target, nextlights):
        if b > a:
          ok = False
          break
      if ok and nextlights not in v:
        q.append((nextlights, d + 1, fb + i))
        v.add(nextlights)
        #print(" " * d, nextlights)
  return 999999

def invertbuttons(buttons, num_lights):
  matrix = []
  for _ in range(num_lights):
    matrix.append([0] * len(buttons))
  for i, b in enumerate(buttons):
    for b2 in b:
      matrix[b2][i] = 1
  for l in matrix:
    print(l)


def main():
  total = 0
  total2 = 0
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.rstrip().split(" ")
      indicators = tuple(True if i == "#" else False for i in line[0][1:-1])
      joltage = tuple(int(i) for i in line[-1][1:-1].split(","))
      line = tuple(l[1:-1].split(",") for l in line[1:-1])
      buttons = [set(int(i) for i in l) for l in line]
      buttons.sort(key = lambda x: -len(x))
      #print(indicators)
      #print(joltage)
      #print(buttons)
      total += bfs(indicators, buttons)
      invertbuttons(buttons, len(indicators))
      #total2 += bfs2(joltage, buttons)
      print("----")
  print('part 1', total)
  print('part 2', total2)



if __name__ == "__main__":
  main()
