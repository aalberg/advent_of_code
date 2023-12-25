import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time
import queue
import heapq

PART = 2
TEST = 0
PROBLEM = 17
in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_pattern = "test%d_2.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)
NUMS = "0123456789"

grid = []
visited = {}
visited2 = []

def inbounds(x, y):
  return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

def reverse_of(d1, d2):
  return d1[0] == -1 * d2[0] and d1[1] == -1 * d2[1]

def get_valid_moves(cur, cur_h):
  valid_moves = []
  for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
    cd = tuple([cur[2], cur[3]])
    if PART == 1 and d == cd and cur[4] == 3:
      continue
    if PART == 2:
      if cd != (0, 0) and d != cd and cur[4] < 4:
        continue
      elif d == cd and cur[4] == 10:
        continue
    if reverse_of(d, cd):
      continue
    new = [cur[0] + d[0], cur[1] + d[1], d[0], d[1], 0]
    if not inbounds(new[0], new[1]):
      continue
    if d == cd:
      new[4] = cur[4] + 1
    else:
      new[4] = 1
    new_heat = cur_h + grid[new[1]][new[0]]
    valid_moves.append(tuple([new_heat, tuple(new)]))
  return valid_moves

def main():
  with open(in_file, 'r') as f:
    for line in f:
      line = line.rstrip()
      grid.append([int(i) for i in line])

  # heat, (x, y, dx, dy, steps)
  frontier = []
  heapq.heappush(frontier, (0, (0, 0, 0, 0, 0)))
  visited[(0, 0, 0, 0, 0)] = 0
  for i in range(len(grid)):
    visited2.append([2000000] * len(grid[0]))
  visited2[0][0] = 0
  last = None
  last_h = 0
  i = 0
  while len(frontier) > 0 and i <= 10**7:
    cur = heapq.heappop(frontier)
    if cur[1][0] == len(grid[0]) - 1 and cur[1][1] == len(grid) - 1 and (PART == 1 or cur[1][4] >= 4):
      last = cur[1]
      last_h = cur[0]
      break
    adj = get_valid_moves(cur[1], cur[0])
    for a in adj:
      h = a[0]
      state = a[1]

      if state not in visited:
        visited[state] = h
        visited2[state[1]][state[0]] = min(visited2[state[1]][state[0]], h)
        heapq.heappush(frontier, a)
    # print(cur, "|", adj)
    # print(frontier)
    # print(visited)
    # print("---------")
    i += 1
  print(last, last_h, i, len(visited))

if __name__=="__main__":
  start_time2 = time.time()
  main()
  print("--- overall: %s seconds ---" % (time.time() - start_time2))
