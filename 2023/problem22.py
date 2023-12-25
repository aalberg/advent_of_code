import bisect
from collections import defaultdict
from collections import deque
from collections import namedtuple
import functools
import math
import os
import time


PART = 1
TEST = 0
PROBLEM = 22
in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_pattern = "test%d.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)
NUMS = "0123456789"

occupied = {}
supporting = defaultdict(dict)
deps = defaultdict(list)

def nextline(f):
  line = f.readline()
  if not line:
    return ""
  line = line.rstrip()
  return line

def inbounds(x, y):
  return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

def make_brick(bs, be):
  brick = []
  if bs[0] != be[0]:
    for x in range(bs[0], be[0] + 1):
      brick.append([x, bs[1], bs[2]])
  elif bs[1] != be[1]:
    for y in range(bs[1], be[1] + 1):
      brick.append([bs[0], y, bs[2]])
  elif bs[2] != be[2]:
    for z in range(bs[2], be[2] + 1):
      brick.append([bs[0], bs[1], z])
  else:
    brick.append(bs)
  return brick

def can_fall(brick):
  touching = {}
  for cube in brick:
    if cube[2] <= 1:
      return False, {}
    c = (cube[0], cube[1], cube[2] - 1)
    if c in occupied:
      touching[occupied[c]] = True
  return len(touching) == 0, touching

def can_fall_ignoring(ignore, self_index):
  if len(deps[self_index]) == 1 and ignore in deps[self_index]:
    return True
  return False

def freeze_brick(brick, i):
  for c in brick:
    occupied[tuple(c)] = i

def drop_bricks(bricks):
  sb = sorted(bricks, key=lambda b: min((c[2] for c in b)))
  for i, brick in enumerate(sb):
    can, t = can_fall(brick)
    while can:
      for j in range(len(brick)):
        brick[j][2] -= 1
      can, t = can_fall(brick)
    deps[i] = t
    for dep in t.keys():
      supporting[dep][i] = True
    freeze_brick(brick, i)
  return sb

def main():
  before_falling = []
  with open(in_file, 'r') as f:
    for i, line in enumerate(f):
      line = line.rstrip().split("~")
      if len(line) == 0:
        continue
      bs, be = [int(i) for i in line[0].split(",")], [int(i) for i in line[1].split(",")]
      before_falling.append(make_brick(bs, be))
  after_falling = drop_bricks(before_falling)

  total = 0
  can_delete = {}
  for to_delete in range(len(after_falling)):
    can_remove = True
    for j, brick in enumerate(after_falling):
      if can_fall_ignoring(to_delete, j):
        can_remove = False
        #print("can't remove", to_delete, "because", j, after_falling[to_delete], brick)
    if can_remove:
      can_delete[to_delete] = True
      #print("can remove", to_delete)
      total += 1
  print("part 1", total)
  
  # print("supporting", supporting)
  # print("deps", deps)
  fall_counts = {}
  for to_delete in range(len(after_falling)):
  #for to_delete in range(1, 3):
    if to_delete in can_delete:
      # print("skipping", to_delete)
      fall_counts[to_delete] = 0
      continue

    to_test = deque()
    for dep in supporting[to_delete]:
      to_test.append(dep)
    
    would_fall = {to_delete: True}
    while len(to_test) > 0:
      dep = to_test.popleft()
      if dep in would_fall:
        continue
      dep_would_fall = True
      for support in deps[dep]:
        if support not in would_fall:
          dep_would_fall = False
          break
      if dep_would_fall:
        would_fall[dep] = True
        for new_dep in supporting[dep]:
          to_test.append(new_dep)
    fall_counts[to_delete] = len(would_fall) - 1
  total = sum((v for _, v in fall_counts.items()))
  print("part 2", total)

if __name__=="__main__":
  main()
