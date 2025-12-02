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
PROBLEM = 21
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"
DIRS_KEYPAD = [(0, -1), (1, 0), (0, 1), (-1, 0)]
DIRS_DIRECTIONS = [(1, 0), (0, 1), (0, -1), (-1, 0)]
NUM_ROBOTS = 1 if PART == 1 else 25

grid = []
e = []
layout_keypad = {
    "0": (1, 3),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "A": (2, 3)
}
layout_directions = {
  "^": (1, 0),
  ">": (2, 1),
  "v": (1, 1),
  "<": (0, 1),
  "A": (2, 0),
}
arrow_to_dir = {
  "A": (0, 0),
  ">": (1, 0),
  "v": (0, 1),
  "<": (-1, 0),
  "^": (0, -1),
}

def delta(p1, p2):
  return (p2[0]-p1[0], p2[1]-p1[1])

def delta_to_dirs(p1, p2, prio, bad_sq=None):
  d = delta(p1, p2)
  presses = ""
  if bad_sq and d[0] < 0 and not (p1[1] == bad_sq[1] and p2[0] == bad_sq[0]):
    presses += "<"*abs(d[0])
    d = (0, d[1])
  if bad_sq and d[1] > 0 and not (p1[0] == bad_sq[0] and p2[1] == bad_sq[1]):
    presses += "v"*abs(d[1])
    d = (d[0], 0)
  #elif bad_sq:
  #  print("override", p1, p2, bad_sq)
  for p in prio:
    if p[0] > 0 and d[0] > 0:
      presses += ">"*abs(d[0])
    elif p[0] < 0 and d[0] < 0:
      presses += "<"*abs(d[0])
    elif p[1] > 0 and d[1] > 0:
      presses += "v"*abs(d[1])
    elif p[1] < 0 and d[1] < 0:
      presses += "^"*abs(d[1])
  return presses + "A"
map_keypad = {}
for k, p in layout_keypad.items():
  map_keypad[k] = {}
  for k2, p2 in layout_keypad.items():
    map_keypad[k][k2] = delta_to_dirs(p, p2, DIRS_KEYPAD, (0, 3))
map_directions = {}
for k, p in layout_directions.items():
  map_directions[k] = {}
  for k2, p2 in layout_directions.items():
    map_directions[k][k2] = delta_to_dirs(p, p2, DIRS_DIRECTIONS)
# print(map_keypad)
# print(map_directions)

def numeric(code):
  return int(code[:-1])

def inbounds(x, y):
  return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def solve_dirpad(code):
  dirpad_directions = "A"
  for i, c in enumerate(code[:-1]):
    dirpad_directions += map_directions[c][code[i+1]]
  print("dirpad: ", dirpad_directions)
  return dirpad_directions

@functools.cache
def solve_subseq(code, depth):
  cur_directions = "A"
  for i, c in enumerate(code[:-1]):
    cur_directions += map_directions[c][code[i+1]]
  return cur_directions

def complexity(code):
  print("code", code)
  n = numeric(code)
  code = "A" + code
  keypress_directions = ""
  for i, c in enumerate(code[:-1]):
    keypress_directions += map_keypad[c][code[i+1]]
  print("keypad: ", keypress_directions)

  cur_directions = "A"
  prev_directions = keypress_directions

  for r in range(NUM_ROBOTS):
    seq_ends = []
    a_found = 0
    i = 1
    while i < len(prev_directions):
      print(i, prev_directions[i])
      if prev_directions[i] == "A":
        a_found += 1
        while i < len(prev_directions) and prev_directions[i] == "A":
          i += 1
        if a_found == 2:
          seq_ends.append(i)
          a_found = 0
      else:
        i += 1
    print(seq_ends)
    # cur_directions = solve_subseq("A" + prev_directions[:seq_ends[0]])
    # for i in range(1, len(seq_ends)):
    #   cur_directions += solve_subseq("A" + prev_directions[seq_ends[i-1]:seq_ends[i]])

    cur_directions = solve_subseq(prev_directions)
    print("dirpad: ", r, len(cur_directions), cur_directions)
    prev_directions = cur_directions

  len_my_directions = 0
  for i, c in enumerate(cur_directions[:-1]):
    len_my_directions += len(map_directions[c][cur_directions[i+1]])
  print("my    : ", len_my_directions)

  print(f"code total: {len_my_directions} {n} {len_my_directions * n}")
  return len_my_directions * n

def main():
  total = 0
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.rstrip()
      total += complexity(line)
  print(f"total {total}")




if __name__ == "__main__":
  main()
