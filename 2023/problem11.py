import bisect
import os
import re

TEST = 0
PROBLEM = 11
in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_pattern = "test%d.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)

def main():
  galaxies = {}
  x_max = 0
  y_max = 0
  with open(in_file, 'r') as f:
    for y, line in enumerate(f):
      line = line.rstrip()
      x_max = len(line)
      y_max = y + 1
      for x in [i.start(0) for i in re.finditer("#", line)]:
        galaxies[(x, y)] = True

  doubled_x = sorted(list(filter(lambda i: i not in
      {x: True for (x, _) in galaxies.keys()}, (x for x in range(x_max)))))
  doubled_y = sorted(list(filter(lambda i: i not in
      {y: True for (_, y) in galaxies.keys()}, (y for y in range(y_max)))))
  gl = list(galaxies.keys())
  total = 0
  total2 = 0
  for i in range(len(gl) - 1):
    for j in range(i + 1, len(gl)):
      x, y = gl[i]
      x2, y2 = gl[j]
      d = abs(x - x2) + abs(y - y2)
      s = abs(bisect.bisect(doubled_x, x) - bisect.bisect(doubled_x, x2)) + \
          abs(bisect.bisect(doubled_y, y) - bisect.bisect(doubled_y, y2))
      total += d + s
      total2 += d + (10**6 - 1) * s
  print(total, total2)


if __name__=="__main__":
  main()
