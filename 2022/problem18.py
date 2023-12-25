import os
from collections import deque

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2022\\"
in_file = os.path.join(in_dir, "input18.txt")

grid = {}
surface = {}
q = deque()
surfacearea = 0


def face_dir(i):
  sign = -1 if i < 3 else 1
  x = sign if i % 3 == 0 else 0
  y = sign if i % 3 == 1 else 0
  z = sign if i % 3 == 2 else 0
  return (x, y, z)


def face_adj(coord):
  #print("face_adj", coord)
  for i in range(6):
    d = face_dir(i)
    new_coord = tuple([coord[j] + d[j] for j in range(3)])
    #print("face_adj2", new_coord)
    yield new_coord


def edge_dir(i):
  sign1 = -1 if i % 6 < 3 else 1
  sign2 = -1 if i < 6 else 1
  axes = i % 3
  if axes == 0:
    return (sign1, sign2, 0)
  elif axes == 1:
    return (sign1, 0, sign2)
  else:
    return (0, sign1, sign2)


def edge_adj(coord):
  for i in range(12):
    d = edge_dir(i)
    yield tuple([coord[j] + d[j] for j in range(3)])


def connected(c1, c2):
  delta = [c1[i] - c2[i] for i in range(3)]
  distance = sum([abs(d) for d in delta])
  if distance == 1:
    return True
  if distance > 2:
    return False
  moves = []
  for j in range(3):
    if delta[j] != 0:
      moves.append(j)
  for m in moves:
    cand = list(c2)
    cand[m] += delta[m]
    if tuple(cand) not in grid:
      return True
  return False

# def near_cystal(coord):
#   for i in range(6):
#     d = face_dir(i)
#     newcoord = tuple([coord[j] + d[j] for j in range(3)])
#     if newcoord in grid:
#       return True

def try_visit(coord):
  global surfacearea
  if coord in surface or coord in grid:
    return
  near_crystal = False
  for new_coord in face_adj(coord):
    #print("nc", new_coord)
    if new_coord in grid:
      #print("hi")
      surfacearea += 1
      near_crystal = True
  if near_crystal:
    q.append(coord)
    surface[coord] = True
  #   print("adding", coord, surfacearea)
  # else:
  #   print("fail  ", coord)


# Flood fill/BFS around the surface from that start point
def trace_surface_from(coord):
  global surfacearea
  print("tracing from", coord)
  try_visit(coord)
  while len(q):
    coord = q.popleft()
    #print("processing", coord)
    for new_coord in face_adj(coord):
      try_visit(new_coord)
    for new_coord in edge_adj(coord):
      if connected(coord, new_coord):
        try_visit(new_coord)
  print("area from", coord, ":", surfacearea)
  surfacearea = 0


def main():
  with open(in_file, 'r') as f:
    for line in f:
      line = line.rstrip().split(",")
      if len(line) == 0:
        break
      coord = (int(line[0]), int(line[1]), int(line[2]))
      grid[coord] = True

  # area = 0
  # Find a random starting point.
  done = False
  for coord in grid:
    for new_coord in face_adj(coord):
      if new_coord not in grid and new_coord not in surface:
        # area += 1
        trace_surface_from(new_coord)
  # print(area)

if __name__=="__main__":
  main()
