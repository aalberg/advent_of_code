import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time

PART = 1
TEST = 1
PROBLEM = 24
in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_pattern = "test%d.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)
NUMS = "0123456789"

stones = []
TEST_MIN = 7 if TEST == 1 else 200000000000000
TEST_MAX = 27 if TEST == 1 else 400000000000000

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

def does_intersect_xy(line1, line2):
  t, i1, i2 = intercept_xy(line1, line2)
  #print(t, line1, i1, line2, i2)
  return t and t[0] >= 0 and t[1] >= 0 and inbounds(i1[0], i1[1])

def inbounds(x, y):
  return x >= TEST_MIN and x <= TEST_MAX and y >= TEST_MIN and y <= TEST_MAX

def intercept_xyz(line1, line2):
  t, i1, i2 = intercept_xy(line1, line2)
  #print(t, i1, i2)
  if not t:
    return None, None, None
  for time in t:
    if time < 0:
      return None, None, None
  i1, i2 = line1.pos_at(t[0]), line2.pos_at(t[1])
  if abs(i1[2] - i2[2]) > .01:
    return None, None, None
  return t, i1, i2

def z_dist_at_xy_intercept(line1, line2):
  t, i1, i2 = intercept_xy(line1, line2)
  #print(t, i1, i2)
  if not t:
    return None, None, None
  for time in t:
    if time < 0:
      return None, None, None
  i1, i2 = line1.pos_at(t[0]), line2.pos_at(t[1])
  return i1[2] - i2[2], t, i1, i2


EPSILON = .01 if TEST == 1 else 100
def close_to(p1, p2):
  return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2]) < EPSILON

def test_velocity2(test_v):
  line1, line2 = stones[0].v_rel(test_v), stones[1].v_rel(test_v)
  t, i1, i2 = intercept_xy(line1, line2)
  if not t or t[0] < 0 or t[1] < 0:
    return None, None, None
  i1, i2 = line1.pos_at(t[0]), line2.pos_at(t[1])

  # print(test_v, i1, i2, t)
  # print(test_v, line1, line2)
  dz = i1[2] - i2[2]
  vz = 0
  if abs(dz) > .0001:
    vz = dz / (t[0] - t[1])
    #print("new_vz", vz)
  test_v = (test_v[0], test_v[1], vz)
  

  line1, line2 = stones[0].v_rel(test_v), stones[1].v_rel(test_v)
  i1, i2 = line1.pos_at(t[0]), line2.pos_at(t[1])
  # print(test_v, line1, line2)
  # print(test_v, i1, i2, close_to(i1, i2))
  # old_intercepts = 
  intercepts = [i1, i2]
  #print(test_v, intercepts)
  for i in range(2, min(len(stones), 4)):
    line3 = stones[i].v_rel(test_v)
    new_times, _, i3 = intercept_xyz(line1, line3)
    if not new_times or not close_to(i1, i3):
      return None, None, None
    t.append(new_times[1])
    intercepts.append(i3)
  #print("OK", t, intercepts)
  return t, intercepts, test_v

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

  LIMIT = 5
  X_CENTER = 0
  Y_CENTER = 0
  if TEST == 0:
    LIMIT = 1
    X_CENTER = 28
    Y_CENTER = -286
  # for vx in range(-LIMIT, LIMIT+1):
  #   for vy in range(-LIMIT, LIMIT+1):
  #     for vz in range(-LIMIT, LIMIT+1):
  #       test_v = (vx, vy, vz)
  #       t, i1 = test_velocity(test_v)
  #       if t:
  #         print(test_v, t, i1)
  #         for i, time in enumerate(t):
  #           print("  ", i, stones[i].pos_at(time))
  #         rock = Line3(i1[0], test_v)
  #         minus_b = rock.pos_at(t[0])
  #         print("part 2: ", test_v, minus_b, sum(minus_b))
  #   print("x", vx)

  for vx in range(-LIMIT + X_CENTER, LIMIT+1 + X_CENTER):
    for vy in range(-LIMIT + Y_CENTER, LIMIT+1 + Y_CENTER):
      test_v = (vx, vy, 0)
      t, intercepts, new_v = test_velocity2(test_v)
      if t:
        print(new_v, t, intercepts)
        for i, time in enumerate(t):
          print("  ", i, time, stones[i].pos_at(time), intercepts[i], sum(round(v) for v in intercepts[i]))
        # for i in range(len(intercepts)):
        #   rock = Line3(intercepts[i], new_v)
        #   minus_b = rock.pos_at(t[i])
        #   print("part 2: ", new_v, minus_b, sum(minus_b))
    #print("x", vx)

  # test_v = (28, -286, 123.0)
  # t, i1, new_v = test_velocity2(test_v)
  # print()



if __name__=="__main__":
  start = time.perf_counter()
  main()
  duration = time.perf_counter() - start
  print('Time:', duration)
