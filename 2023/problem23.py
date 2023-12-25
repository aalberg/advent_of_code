import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time

PART = 2
TEST = 0
PROBLEM = 23
in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_pattern = "test%d.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)
NUMS = "0123456789"

grid = []
x_max = 0
y_max = 0
visited = {}
graph = {}

slopes = {
  ".": [(1, 0), (-1, 0), (0, 1), (0, -1)],
  "^": [(0, -1)],
  "v": [(0, 1)],
  ">": [(1, 0)],
  "<": [(-1, 0)],
}

def inbounds(x, y):
  return x >= 0 and x < x_max and y >= 0 and y < y_max

def get_adj(cur, part):
  valid = []
  possible = [(1, 0), (-1, 0), (0, 1), (0, -1)] if part == 2 else slopes[grid[cur[1]][cur[0]]]
  for d in possible:
    new = (cur[0] + d[0], cur[1] + d[1])
    if inbounds(new[0], new[1]) and grid[new[1]][new[0]] in ".v^<>":
      #print(new)
      valid.append(new)
  return valid

def cardinality(cur):
  return len(get_adj(cur, 2))

def find_critical_nodes():
  nodes = []
  for x in range(x_max):
    for y in range(y_max):
      cur = (x, y)
      if grid[y][x] in ".v^<>" and cardinality(cur) > 2:
        nodes.append(cur)
  return nodes

def build_graph(start, target, part):
  graph_nodes = find_critical_nodes()
  graph_nodes.append(start)
  graph_nodes.append(target)
  for g in graph_nodes:
    graph[g] = {}

  for start_node in graph_nodes:
    visited = {start_node : True}
    frontier = deque()
    frontier.append((start_node, 0))
    while len(frontier) > 0:
      cur, d = frontier.popleft()
      if cur != start_node and cur in graph:
        graph[start_node][cur] = d
      else:
        next_cur = get_adj(cur, part)
        for n in next_cur:
          if n not in visited:
            frontier.append((n, d + 1))
            visited[n] = True

def dfs_graph(cur, d, target):
  if cur == target:
    return d
  max_dist = 0
  for n in graph[cur].keys():
    if n not in visited:
      visited[n] = True
      max_dist = max(max_dist, dfs_graph(n, d + graph[cur][n], target))
      del visited[n]
  return max_dist

def main():
  global x_max
  global y_max
  with open(in_file, 'r') as f:
    for line in f:
      line = line.rstrip()
      grid.append(line)
  y_max = len(grid)
  x_max = len(grid[0])

  start = (grid[0].find("."), 0)
  target = (grid[y_max - 1].find("."), y_max - 1)
  print(start, target)

  build_graph(start, target, 1)
  print(dfs_graph(start, 0, target))
  build_graph(start, target, 2)
  print(dfs_graph(start, 0, target))

if __name__=="__main__":
  main()
