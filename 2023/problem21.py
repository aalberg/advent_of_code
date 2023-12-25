import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time

PART = 1
TEST = 0
PROBLEM = 21
in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_pattern = "test%d.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)

grid = []
x_max = 0
y_max = 0

def inbounds(x, y):
  return x >= 0 and x < x_max and y >= 0 and y < y_max

def adj(cur):
  valid = []
  for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    new_cur = (cur[0] + d[0], cur[1] + d[1])
    if inbounds(new_cur[0], new_cur[1]) and grid[new_cur[1]][new_cur[0]] in ".S":
    #if grid[new_cur[1] % y_max][new_cur[0] % x_max] in ".S":
      valid.append(new_cur)
  return valid

def adj2(cur):
  valid = []
  for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    new_cur = (cur[0] + d[0], cur[1] + d[1])
    if grid[new_cur[1] % y_max][new_cur[0] % x_max] in ".S":
      valid.append(new_cur)
  return valid

MAX_DIST = 10000

def floodfill(start, wrap, max_steps=-1):
  frontier = deque()
  frontier.append((start, 0))
  visited = {}
  visited[start] = 0

  while len(frontier) > 0:
    cur, d = frontier.popleft()
    if max_steps >= 0 and d >= max_steps:
      continue
    next_cur = None
    if not wrap:
      next_cur = adj(cur)
    else:
      next_cur = adj2(cur)
    for n in next_cur:
      if n not in visited:
        frontier.append((n, d + 1))
        visited[n] = d + 1
  return visited

def print_visited(visited):
  for x in range(x_max):
    output = ""
    for y in range(y_max):
      if (x, y) in visited:
        output += f" {visited[(x, y)]:3}"
      else:
        output += "   ."
    print(output)

def count_reachable(visited, max_dist):
  if max_dist < 0:
    return 0, {}
  reachable = 0
  spaces = {}
  for k, d in visited.items():
    if d <= max_dist and d % 2 == max_dist % 2:
      reachable += 1
      spaces[k] = True
  return reachable, spaces

def start_edge_cord(d, i):
  if d[0] == 0:
    if d[1] == 1:
      return (x_max - 1, i)
    else:
      return (0, i)
  else:
    if d[0] == 1:
      return (i, y_max - 1)
    else:
      return (i, 0)

def stop_edge_cord(d, i):
  if d[0] == 0:
    if d[1] == -1:
      return (x_max - 1, i)
    else:
      return (0, i)
  else:
    if d[0] == -1:
      return (i, y_max - 1)
    else:
      return (i, 0)

def propagate_edge(d, cur, edge_maps):
  prop_edge = [10**4] * x_max
  sources = [0] * x_max
  for i_s in range(x_max):
    ymap = edge_maps[stop_edge_cord(d, i_s)]
    for i_t in range(x_max):
      #print(cur[i_s], ymap[start_edge_cord(d, i_t)])
      dist = cur[i_s] + ymap[start_edge_cord(d, i_t)] + 1
      if dist < prop_edge[i_t]:
        prop_edge[i_t] = dist
        sources[i_t] = i_s
  return prop_edge, sources

def main():
  global x_max
  global y_max
  start = (0, 0)
  with open(in_file, 'r') as f:
    for i, line in enumerate(f):
      line = line.rstrip()
      grid.append(line)
      if "S" in line:
        start = (i, line.find("S"))
  y_max = len(grid)
  x_max = len(grid[0])

  # Part 1
  base = floodfill(start, False, 64)
  print("part 1: ", count_reachable(base, 64)[0])

  # Brute force part 2
  if MAX_DIST < 10000:
    base = floodfill(start, True, MAX_DIST)
    print("part 2: ", count_reachable(base, MAX_DIST)[0])
  else:
    print("part 2: skipping")

  #print_visited(base)

  # Part 2
  base = floodfill(start, False)
  edge_maps = {}
  max_d = {}
  for x in range(x_max):
    new_start = (x, 0)
    edge_maps[new_start] = floodfill(new_start, False)
    max_d[new_start] = max((d for d in edge_maps[new_start].values()))
    new_start = (x, y_max - 1)
    edge_maps[new_start] = floodfill(new_start, False)
    max_d[new_start] = max((d for d in edge_maps[new_start].values()))

  for y in range(1, y_max - 1):
    new_start = (0, y)
    edge_maps[new_start] = floodfill(new_start, False)
    max_d[new_start] = max((d for d in edge_maps[new_start].values()))
    new_start = (x_max - 1, y)
    edge_maps[new_start] = floodfill(new_start, False)
    max_d[new_start] = max((d for d in edge_maps[new_start].values()))

  #print(sorted(edge_maps.keys()))
  print("=========")
  # print_visited(edge_maps[(0, 0)])
  # print_visited(edge_maps[(0, y_max-1)])
  # print_visited(edge_maps[(x_max-1, 0)])
  # print_visited(edge_maps[(x_max-1, y_max-1)])
  # print(max_d[(0, 0)])
  # for k, v in max_d.items():
  #   if v == 21:
  #     print_visited(edge_maps[k])
  # print(max(v for v in max_d.values()))

  # Handle corners
  grid_parity = x_max % 2
  total_reachable = 0
  for corner, base_corner in zip([(x_max-1, y_max-1), (0, y_max-1), (0, 0), (x_max-1, 0)], [(0, 0), (x_max-1, 0), (x_max-1, y_max-1), (0, y_max-1)]):
    print("--------")
    initial_corner_steps = base[base_corner] + 2
    full_enclose_steps = (MAX_DIST - initial_corner_steps) - max_d[corner]
    k = max(-1, math.floor(full_enclose_steps/x_max))
    remaining = (MAX_DIST - initial_corner_steps) - (k+1)*x_max
    print("steps math", initial_corner_steps, k, full_enclose_steps, remaining, remaining - x_max)

    if remaining <= 0:
      continue

    e = edge_maps[corner]
    #print_visited(e)
    
    # Handle parital plots
    # First layer we can't fully cover 
    corner_reachable = 0
    partial = k + 2
    reachable_partial, _ = count_reachable(e, remaining)
    subtotal = partial * reachable_partial
    corner_reachable += subtotal
    # Go out one more layer and see if we can cover any of these
    partial2 = k + 3
    reachable_partial2, _ = count_reachable(e, remaining - x_max)
    subtotal2 = partial2 * reachable_partial2
    corner_reachable += subtotal2
    print("reachable_partial", subtotal, subtotal2, reachable_partial, partial, reachable_partial2, partial2)


    # Handle fully enclosed plots
    if k > 0:
      initial_parity = initial_corner_steps % 2
      print("parity", grid_parity, initial_parity)
      enclosed = int((k+2) * (k+1) / 2)
      if grid_parity == 0:
        reachable_enclose, _ = count_reachable(e, MAX_DIST + initial_parity)
        subtotal = enclosed * reachable_enclose
        corner_reachable += subtotal
        print("reachable_enclose", subtotal, reachable_enclose, enclosed)
      else:
        enclosed_even = (math.floor((k+1)/2) + 1) * math.floor((k+1)/2)
        enclosed_odd = enclosed - enclosed_even
        reachable_even, _ = count_reachable(e, MAX_DIST + grid_parity)
        reachable_odd, _ = count_reachable(e, MAX_DIST)
        subtotal = enclosed_even * reachable_even + enclosed_odd * reachable_odd
        corner_reachable += subtotal
        print("reachable_enclose", subtotal, reachable_even, enclosed_even, reachable_odd, enclosed_odd)

    print("corner_reachable", corner_reachable)
    total_reachable += corner_reachable
  print("total", total_reachable)

  # Handle axes
  for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
  #for d in [(0, -1)]:
    base_edge = [base[start_edge_cord(d, y)] for y in range(y_max)]
    print("0", base_edge)

    prop_edge = base_edge
    prev_delta = [0] * x_max
    delta = [1] * x_max
    k = 0
    min_max_d = min(max_d[start_edge_cord(d, y)] for y in range(y_max))
    while prev_delta != delta:
      prev_delta = delta
      cur = prop_edge
      prop_edge, sources = propagate_edge(d, cur, edge_maps)
      if max(prop_edge) + min_max_d < MAX_DIST:
        k += 1

      delta = [prop_edge[i] - cur[i] for i in range(len(prop_edge))]
      print(" ", delta)
      print(" ", sources)
      print(k, prop_edge)

    initial_edge_steps = min(prop_edge)
    initial_edge_starts = []
    for i, p in enumerate(prop_edge):
      if p == initial_edge_steps:
        initial_edge_starts.append(i)
    min_max_d = min(max_d[start_edge_cord(d, p)] for p in initial_edge_starts)
    
    full_enclose_steps = (MAX_DIST - initial_edge_steps) - min_max_d
    if full_enclose_steps > 0:
      new_k = math.floor(full_enclose_steps/x_max)
    remaining = (MAX_DIST - initial_edge_steps) - (new_k+1)*x_max
    print("edge steps math", initial_edge_steps, k, full_enclose_steps, remaining, initial_edge_starts)

    # Handle fully enclosed plots
    edge_reachable = 0
    if k > 0:
      initial_parity = initial_edge_steps % 2
      print("parity", grid_parity, initial_parity)
      enclosed = k + new_k
      if grid_parity == 0:
        reachable_enclose = {}
        for p in initial_edge_starts:
          _, subset = count_reachable(edge_maps[p], MAX_DIST + initial_parity)
          reachable_enclose |= subset
        reachable_enclose = len(reachable_enclose.keys())
        subtotal = enclosed * reachable_enclose
        edge_reachable += subtotal
        print("reachable_enclose", subtotal, reachable_enclose, enclosed)
      else:
        enclosed_odd = math.floor((enclosed+1)/2)
        enclosed_even = enclosed - enclosed_odd
        reachable_even = {}
        reachable_odd = {}
        for p in initial_edge_starts:
          e = edge_maps[start_edge_cord(d, p)]
          _, subset_even = count_reachable(e, MAX_DIST)
          _, subset_odd = count_reachable(e, MAX_DIST + grid_parity)
          reachable_even |= subset_even
          reachable_odd |= subset_odd
        reachable_even = len(reachable_even.keys())
        reachable_odd = len(reachable_odd.keys())
        subtotal = enclosed_even * reachable_even + enclosed_odd * reachable_odd
        edge_reachable += subtotal
        #print("enclosed math", enclosed, enclosed_even, enclosed_odd)
        print("reachable_enclose", subtotal, reachable_even, enclosed_even, reachable_odd, enclosed_odd)

      # Handle parital plots
      print("remaining", remaining)
      while remaining > 0:
        reachable_partial = {}
        for p in initial_edge_starts:
          e = edge_maps[start_edge_cord(d, p)]
          _, subset = count_reachable(e, remaining)
          reachable_partial |= subset
        reachable_partial = len(reachable_partial.keys())
        print("  ", reachable_partial)
        edge_reachable += reachable_partial
        remaining -= x_max

    print("edge_reachable", edge_reachable)
    total_reachable += edge_reachable

  #print_visited(edge_maps[(x_max-1, 24)])

  print("total2", total_reachable)

if __name__=="__main__":
  main()
