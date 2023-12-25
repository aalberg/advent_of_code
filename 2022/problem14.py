import os

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2022\\"
in_file = os.path.join(in_dir, "input14.txt")

maxy = 0
grid = {}

def down(cur):
  return (cur[0], cur[1] + 1)

def downleft(cur):
  return (cur[0] - 1, cur[1] + 1)

def downright(cur):
  return (cur[0] + 1, cur[1] + 1)

def cmp(a, b):
  return (a > b) - (a < b)

def cmpcoord(a, b):
  return a[0] == b[0] and a[1] == b[1]

def gridinsert(coord):
  global maxy
  maxy = max(maxy, coord[1])
  grid[tuple(coord)] = True

def drawline(a, b):
  delta = [-cmp(a[i], b[i]) for i in range(2)]
  #print(a, b, delta)
  cur = a
  while not cmpcoord(cur, b):
    #print(cur)
    gridinsert(cur)
    grid[tuple(cur)] = True
    cur = [cur[i] + delta[i] for i in range(2)]
  gridinsert(b)

def placerock():
  cur = (500, 0)
  if cur in grid.keys():
    return False
  while cur[1] <= maxy:
    #print(cur)
    t = down(cur)
    if t not in grid.keys():
      cur = t
      continue
    t = downleft(cur)
    if t not in grid.keys():
      cur = t
      continue
    t = downright(cur)
    if t not in grid.keys():
      cur = t
      continue
    break

  # if cur[1] <= maxy:
  print("placed ", cur)
  grid[cur] = True
  return True
  # else:
  #   print("done   ", cur)
  #   return False

def main():
  with open(in_file, 'r') as f:
    for line in f:
      line = line.rstrip()
      coords = [(int(a[0]), int(a[1])) for a in [c.split(",") for c in line.split(" -> ")]]
      for i in range(len(coords) - 1):
        drawline(coords[i], coords[i + 1])
      print("")
    print(grid, "\n", maxy)
  count = 0
  while True:
    placed = placerock()
    if not placed:
      break
    count += 1
  print(count)

if __name__=="__main__":
  main()
