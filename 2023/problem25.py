import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time
import random

PART = 1
TEST = 0
PROBLEM = 25
in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_pattern = "test%d.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)
NUMS = "0123456789"

graph = defaultdict(dict)
saved_graph = None

def merge(v1, v2):
  for adj in graph[v1].keys():
    if adj in graph[v2]:
      graph[v2][adj] += graph[v1][adj]
      graph[adj][v2] += graph[v1][adj]
    elif adj != v2:
      graph[v2][adj] = graph[v1][adj]
      graph[adj][v2] = graph[v1][adj]
    del graph[adj][v1]
  del graph[v1]

def copy_graph(g):
  graph_copy = defaultdict(dict)
  for k, v in g.items():
    graph_copy[k] = dict(v)
  return graph_copy

def contract(graph):
  childen = defaultdict(list)
  while len(graph) > 2:
    v1 = random.choice(list(graph.keys()))
    v2 = random.choice(list(graph[v1].keys()))
    # while v1 == v2:
    #   v2 = random.choice(list(graph.keys()))
    merge(v1, v2)
    childen[v2].append(v1)
  return childen

def karger():
  global graph
  global saved_graph
  best_result = 1000
  result = best_result
  saved_graph = copy_graph(graph)
  start, end  = None, None
  while result > 3:
    graph = copy_graph(saved_graph)
    children = contract(graph)
    start = next(iter(graph))
    end = next(iter(graph[start]))
    result = graph[start][end]
    if result < best_result:
      best_result = result
      best_childen = children
      print("new_best", result)#, best_childen)
  
  start = next(iter(graph))
  frontier = deque()
  frontier.append(start)
  count = 0
  while len(frontier) > 0:
    cur = frontier.popleft()
    next_cur = children[cur]
    frontier.extend(next_cur)
    count += 1

  print("count", count, len(saved_graph) - count, count * (len(saved_graph) - count))

  return best_result

def main():
  with open(in_file, 'r') as f:
    for line in f:
      line = line.rstrip().split(": ")    
      s = line[0]
      for e in line[1].split(" "):
        graph[s][e] = 1
        graph[e][s] = 1
  karger()


if __name__=="__main__":
  start = time.perf_counter()
  main()
  duration = time.perf_counter() - start
  print('Time:', duration)
