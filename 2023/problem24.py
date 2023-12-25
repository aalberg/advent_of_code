import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time

TEST = 0
PROBLEM = 24
in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_pattern = "test%d.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)
NUMS = "0123456789"

stones = []
TEST_MIN = 7 if TEST == 1 else 200000000000000
TEST_MAX = 27 if TEST == 1 else 400000000000000

LIMIT = 300 if TEST == 0 else 10
EPSILON = 100 if TEST == 0 else .01
EPSILON2 = .01

class Line3:
  def __init__(self, pos, slope):
    self.pos = tuple(pos)
    self.slope = tuple(slope)

  def slope_xy(self, k = 1):
    return [self.slope[i] * k for i in range(2)]

  def pos_xy(self):
    return self.pos[0:2]

  def pos_xy_at(self, t):
    return [self.pos[i] + self.slope[i]*t for i in range(2)]

  def pos_at(self, t):
    return [self.pos[i] + self.slope[i]*t for i in range(3)]

  def v_rel(self, v):
    return Line3(self.pos, tuple([self.slope[i] - v[i] for i in range(3)]))

  def __str__(self):
    return str(self.pos) + " | " + str(self.slope)

  def __repr__(self):
    return str(self)

def det(matrix):
  return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

def inverse_2d(matrix):
  d = det(matrix)
  if d == 0:
    return None
  return [[matrix[1][1]/d, -matrix[1][0]/d], [-matrix[0][1]/d, matrix[0][0]/d]]

def intercept_xy(line1, line2):
  Ai = inverse_2d(list(zip(line1.slope_xy(), line2.slope_xy(-1))))
  if Ai == None:
    return None, None, None
  b1, b2 = line1.pos_xy(), line2.pos_xy()
  b = [b2[i] - b1[i] for i in range(2)]
  t = [0, 0]
  for i in range(2):
    t[i] = sum(Ai[j][i] * b[j] for j in range(2))
  return t, line1.pos_xy_at(t[0]), line2.pos_xy_at(t[1])

def inbounds(x, y):
  return x >= TEST_MIN and x <= TEST_MAX and y >= TEST_MIN and y <= TEST_MAX

def does_intersect_xy(line1, line2):
  t, i, _ = intercept_xy(line1, line2)
  return t and t[0] >= 0 and t[1] >= 0 and inbounds(i[0], i[1])

def intercept_xyz(line1, line2):
  t, i1, i2 = intercept_xy(line1, line2)
  if not t:
    return None, None, None
  for time in t:
    if time < 0:
      return None, None, None
  i1, i2 = line1.pos_at(t[0]), line2.pos_at(t[1])
  if abs(i1[2] - i2[2]) > EPSILON2:
    return None, None, None
  return t, i1, i2

def close_to(p1, p2):
  return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2]) < EPSILON

def test_velocity2(test_v):
  # Make everything relative to the rock. If this velocity is correct, all the
  # hailstones will intersect at the same point.
  line1, line2 = stones[0].v_rel(test_v), stones[1].v_rel(test_v)

  # Find the xy intersection of the first two stones
  t, i1, i2 = intercept_xy(line1, line2)
  if not t or t[0] < 0 or t[1] < 0:
    return None, None
  i1, i2 = line1.pos_at(t[0]), line2.pos_at(t[1])

  # Calculate the z velocity that would cause these points to intersect in the
  # z dimension as well.
  dz = i1[2] - i2[2]
  vz = 0
  if abs(dz) > EPSILON2:
    vz = dz / (t[0] - t[1])
  test_v = (test_v[0], test_v[1], vz)
  
  # Refind the xyz intersection of the first two stones
  line1, line2 = stones[0].v_rel(test_v), stones[1].v_rel(test_v)
  i1, i2 = line1.pos_at(t[0]), line2.pos_at(t[1])
  intercepts = [i1, i2]

  # Check if this intersection point works for some number of the other stones.
  # We probably only need 3 points, but use more to be safe.
  for i in range(2, min(len(stones), 4)):
    line3 = stones[i].v_rel(test_v)
    new_times, _, i3 = intercept_xyz(line1, line3)
    if not new_times or not close_to(i1, i3):
      return None, None
    t.append(new_times[1])
    intercepts.append(i3)
  return intercepts, test_v

def main():
  with open(in_file, 'r') as f:
    for line in f:
      line = line.rstrip().split(" @ ")
      pos = line[0].split(", ")
      pos = [int(v) for v in pos]
      velocity = line[1].split(", ")
      velocity = [int(v) for v in velocity]
      stones.append(Line3(pos, velocity))

  total = 0
  for i in range(len(stones) - 1):
    for j in range(i + 1, len(stones)):
      if does_intersect_xy(stones[i], stones[j]):
        total += 1
  print("part 1:", total)

  for vx in range(-LIMIT, LIMIT+1):
    for vy in range(-LIMIT, LIMIT+1):
      test_v = (vx, vy, 0)
      intercepts, new_v = test_velocity2(test_v)
      if intercepts:
        print("part 2:", sum(round(v) for v in intercepts[0]))

if __name__=="__main__":
  start = time.perf_counter()
  main()
  duration = time.perf_counter() - start
  print('Time:', duration)
