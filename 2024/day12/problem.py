from collections import deque
import os
import time

PART = 1
TEST = 0
PROBLEM = 12
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

grid = []
e = []
regions = set()


def inbounds(x, y):
  return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def adj(x, y):
  a = []
  for d in DIRS:
    n = (x + d[0], y + d[1])
    a.append(n)
  return a


def flood_fill(x, y):
  e[y][x] = 1
  q = deque()
  q.append((x, y))
  area = 0
  perim = set()
  while len(q) > 0:
    c = q.popleft()
    area += 1
    for d, a in enumerate(adj(c[0], c[1])):
      if inbounds(
          a[0],
          a[1]) and grid[a[1]][a[0]] == grid[c[1]][c[0]] and e[a[1]][a[0]] == 0:
        e[a[1]][a[0]] = 1
        q.append(a)
      if not inbounds(a[0], a[1]) or grid[a[1]][a[0]] != grid[c[1]][c[0]]:
        perim.add((c, d))
  return area, len(perim), count_sides(perim)


def count_sides(perim):
  sides = 0
  while len(perim) > 0:
    c, d = next(iter(perim))
    perim.remove((c, d))
    for nd in [(d - 1) % 4, (d + 1) % 4]:
      n = tuple(c[i] + DIRS[nd][i] for i in range(2))
      while (n, d) in perim:
        perim.remove((n, d))
        n = tuple(n[i] + DIRS[nd][i] for i in range(2))
    sides += 1
  return sides


def main():
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.rstrip()
      grid.append(line)
      e.append([0] * len(line))

  total = 0
  total2 = 0
  # pylint: disable=consider-using-enumerate
  for x in range(len(grid[0])):
    for y in range(len(grid)):
      if e[y][x] == 0:
        area, perim, sides = flood_fill(x, y)
        total += area * perim
        total2 += area * sides
  # pylint: enable=consider-using-enumerate
  print(total)
  print(total2)


if __name__ == "__main__":
  start_time = time.time()
  main()
  print("--- overall: %s seconds ---" % (time.time() - start_time))
