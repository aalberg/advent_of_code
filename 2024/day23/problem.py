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
TEST = 0
PROBLEM = 23
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

graph = defaultdict(set)


def main():
  t_tri = 0
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.rstrip().split("-")
      graph[line[0]].add(line[1])
      graph[line[1]].add(line[0])
      for v1 in graph[line[0]]:
        for v2 in graph[line[1]]:
          if v1 == v2 and (line[0][0] == "t" or line[1][0] == "t" or v1[0][0] == "t"):
            t_tri += 1
  print("part1", t_tri)
  max_clique = set()
  for v, adj_v in graph.items():
    clique = set()
    clique.add(v)
    for v2 in adj_v:
      ok = True
      for c in clique:
        if v2 not in graph[c]:
          ok = False
          break
      if ok:
        clique.add(v2)
    if len(clique) > len(max_clique):
      max_clique = clique
  print("part2", ",".join(sorted(max_clique)))




if __name__ == "__main__":
  main()
