import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time

PART = 2
TEST = 0
PROBLEM = 18
in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_pattern = "test%d.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)
NUMS = "0123456789"

polygon = []
left_poly = []
right_poly = []

def move(cur, left, right, direction, count, cur_turn, prev_turn):
  d = (0, 0)
  if direction == "R":
    d = (1, 0)
  elif direction == "L":
    d = (-1, 0)
  elif direction == "D":
    d = (0, 1)
  elif direction == "U":
    d = (0, -1)

  lc = count
  rc = count
  if prev_turn == "R" and cur_turn == "R":
    lc = count + 1
    rc = count - 1
  elif prev_turn == "L" and cur_turn == "L":
    lc = count - 1
    rc = count + 1
  for i in range(2):
    cur[i] += count * d[i]
    left[i] += lc * d[i]
    right[i] += rc * d[i]

  return cur, left, right

def turn_dir(prev, cur):
  if prev == "U" and cur == "R":
    return "R"
  elif prev == "R" and cur == "D":
    return "R"
  elif prev == "D" and cur == "L":
    return "R"
  elif prev == "L" and cur == "U":
    return "R"
  elif prev == "U" and cur == "L":
    return "L"
  elif prev == "L" and cur == "D":
    return "L"
  elif prev == "D" and cur == "R":
    return "L"
  elif prev == "R" and cur == "U":
    return "L"

def area(p):
  return 0.5 * abs(sum(x0*y1 - x1*y0
                       for ((x0, y0), (x1, y1)) in segments(p)))

def segments(p):
  return zip(p, p[1:] + [p[0]])

def convert_hex(hexcode):
  d = ""
  if hexcode[-1] == "0":
    d = "R"
  elif hexcode[-1] == "1":
    d = "D"
  elif hexcode[-1] == "2":
    d = "L"
  elif hexcode[-1] == "3":
    d = "U"

  val = int(hexcode[0:-1], 16)
  return val, d

def parse_line(line):
  if PART == 1:
    return line[0], int(line[1])
  count, direction = convert_hex(line[2][2:-1])
  return direction, count

def main():
  global x_max, y_max, x_min, y_min
  cur = [0, 0]
  left = [0, 0]
  right = [0, 0]
  lines = None
  with open(in_file, 'r') as f:
    lines = [l.rstrip().split() for l in f.readlines()]

  prev_dir, _ = parse_line(lines[-1])
  prev_turn = turn_dir(prev_dir, parse_line(lines[0])[0])
  for i, line in enumerate(lines):
    direction, count = parse_line(line)

    next_dir, _ = parse_line(lines[(i + 1) % len(lines)])
    cur_turn = turn_dir(direction, next_dir)
    cur, left, right = move(cur, left, right, direction, count, cur_turn, prev_turn)
    polygon.append(tuple(cur))
    left_poly.append(tuple(left))
    right_poly.append(tuple(right))
    prev_dir = direction
    prev_turn = cur_turn
  
  a1 = area(polygon)
  a2 = area(left_poly)
  a3 = area(right_poly)
  # print(polygon)
  # print(left_poly)
  # print(right_poly)
  print(a1)
  print(a2)
  print(a3)
  print("----")
  print(max(a1, a2, a3))

if __name__=="__main__":
  main()
