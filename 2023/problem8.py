import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time

TEST = 0
PROBLEM = 8
in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_pattern = "test%d.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)

turns = ""
network = {}

def traverse(part):
  cur = ["AAA"]
  if part == 2:
    cur = list(filter(lambda x: x[-1] == "A", network.keys()))
  cycle_len = [-1] * len(cur)
  print("start", cur)
  loops = 0
  while True:
    for i, t in enumerate(turns):
      done = True
      for j, c in enumerate(cur):
        if part == 1 and c == "ZZZ":
          return loops * len(turns) + i
        elif part == 2 and c[-1] == "Z":
          cycle_len[j] = loops * len(turns) + i
          print("  done", cur, j, cycle_len)
        if cycle_len[j] == -1:
          done = False
        cur[j] = network[c][0] if t == "L" else network[c][1]
      if done:
        print(cycle_len)
        return math.lcm(*cycle_len)
    loops += 1
  # Impossible
  exit(1)

def main():
  global turns
  with open(in_file, 'r') as f:
    for i, line in enumerate(f):
      line = line.rstrip()
      if i == 0:
        turns = line
        continue
      elif i == 1:
        continue
      line_s = line.split()
      a, b, c = line_s[0], line_s[2][1:-1], line_s[3][:-1]
      network[a] = (b, c)

  print(traverse(1))
  print(traverse(2))

if __name__=="__main__":
  main()
