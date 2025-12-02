import bisect
from collections import defaultdict
from collections import deque
import functools
import heapq
import itertools
import math
import os
import re
import time
import typing

PART = 1
TEST = 0
PROBLEM = 24
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
IN_PATTERN = "test2.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

bool_vals = {}


def nextline(f):
  line = f.readline()
  if not line:
    return ""
  line = line.rstrip()
  return line


def do_op(o1: bool, o2: bool, op):
  if op == "AND":
    return o1 and o2
  if op == "OR":
    return o1 or o2
  if op == "XOR":
    return o1 ^ o2


#@functools.cache
def recursive_op(bv, wire, p = False, depth=0) -> bool:
  val = bv[wire]
  if p:
    print(" " * depth, wire, val)
  if type(val) == bool:
    return val
  return do_op(
      recursive_op(bv, val[0], p, depth + 1),
      recursive_op(bv, val[1], p, depth + 1), val[2])

#@functools.cache
def recursive_op2(bv, wire, p = False, depth=0) -> typing.Tuple[bool, set]:
  val = bool_vals[wire]
  if p:
    print(" " * depth, wire, val)
  if type(val) == bool:
    s = set()
    s.add(wire)
    return val, s
  x, xs = recursive_op2(bv, val[0], p, depth + 1)
  y, ys = recursive_op2(bv, val[1], p, depth + 1)
  xs.add(wire)
  return do_op(x, y, val[2]), xs.union(ys)


def num_from_prefix(bv, prefix, p = False):
  output = ""
  for k in sorted(bool_vals.keys()):
    if k[0] == prefix:
      output = ("1" if recursive_op(bv, k, p) else "0") + output
  return int(output, 2)


# def swap_values(bv, x, y):
#   #print(len(bv))
#   new_bv = dict(bv)
#   # x with placeholder
#   if x in new_bv:
#     new_bv["placeholder"] = new_bv[x]
#   for k, old in new_bv.items():
#     if type(old) == tuple and x in old:
#       if x == old[0]:
#         new_bv[k] = ("placeholder", old[1], old[2])
#       elif x == old[1]:
#         new_bv[k] = (old[0], "placeholder", old[2])
#   # y with x
#   if y in new_bv:
#     new_bv[x] = new_bv[y]
#   for k, old in new_bv.items():
#     if type(old) == tuple and y in old:
#       if y == old[0]:
#         new_bv[k] = (x, old[1], old[2])
#       elif y == old[1]:
#         new_bv[k] = (old[0], x, old[2])
#   #placeholder with y
#   if "placeholder" in new_bv:
#     new_bv[y] = new_bv["placeholder"]
#   for k, old in new_bv.items():
#     if type(old) == tuple and "placeholder" in old:
#       if "placeholder" == old[0]:
#         new_bv[k] = (y, old[1], old[2])
#       elif "placeholder" == old[1]:
#         new_bv[k] = (old[0], y, old[2])
#   return new_bv


def swap_values(bv, x, y):
  #print(len(bv))
  new_bv = dict(bv)
  if x in new_bv and y in new_bv:
    new_bv[x], new_bv[y] = new_bv[y], new_bv[x]
  return new_bv


def main():
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    line = "."
    while len(line) > 0:
      line = nextline(f)
      if not line:
        break
      line = [i.strip() for i in line.split(":")]
      bool_vals[line[0]] = bool(int(line[1]))
      #print(line)
    line = "."
    while len(line) > 0:
      line = nextline(f).split()
      if len(line) < 5:
        break
      o1 = line[0]
      o2 = line[2]
      dest = line[4]
      op = line[1]
      bool_vals[dest] = (o1, o2, op)
  x = num_from_prefix(bool_vals, "x")
  y = num_from_prefix(bool_vals, "y")
  z = num_from_prefix(bool_vals, "z")
  print("part1", z)
  print("x", x, bin(x), sep="\t")
  print("y", y, bin(y), sep="\t")
  print("z_tar", x + y, bin(x + y), sep="\t")
  print("z_cur", z, bin(z), sep="\t")
  z_tar_bin = list(reversed(bin(x + y)))
  z_cur_bin = list(reversed(bin(z)))
  cur_bvs = deque()
  cur_bvs.append((set(), bool_vals))
  i = 0
  while len(cur_bvs):
    cur_swaps, cur_bv = cur_bvs.popleft()
    nz = num_from_prefix(cur_bv, "z")
    print("z_cur", nz, bin(nz), cur_swaps, sep="\t")
    z_cur_bin = list(reversed(bin(nz)))
    ok = True
    for i, b in enumerate(z_cur_bin):
      if b != z_tar_bin[i]:
        ok = False
        print("diff at bit", i, b, z_tar_bin[i])
        _, zs1 = recursive_op2(cur_bv, f"z{(i-1):02d}")
        zk = f"z{i:02d}"
        za, zs2 = recursive_op2(cur_bv, zk)

        def test(k):
          return not (k[0] == "x" or k[0] == "y")# or k[0] == "z")
        set_diff = set(filter(test, zs2 - zs1))
        print(sorted(zs1))
        print(sorted(zs2))
        print("set_diff", set_diff)
        #print(bool_vals)
        dep_sets = {}
        for s in set_diff:
          _, a = recursive_op2(cur_bv, s)
          dep_sets[s] = a
        for swap1, swap2 in list(itertools.combinations(set_diff, 2)):
          if swap1 in dep_sets[swap2] or swap2 in dep_sets[swap1]:
            continue
          new_bv = swap_values(cur_bv, swap1, swap2)
          new_za = recursive_op(new_bv, zk)
          #print(swap1, swap2, zk, za, new_za)
          if za != new_za:
            new_swaps = set(cur_swaps)
            new_swaps.add(swap1)
            new_swaps.add(swap2)
            cur_bvs.append((new_swaps, new_bv))
          #print(new_bv)
        #print([(i[0], len(i[1])) for i in cur_bvs])
        break
    if ok:
      print("ok", cur_swaps)
      break


if __name__ == "__main__":
  main()
