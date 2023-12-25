import os
import time

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2022\\"
in_file = os.path.join(in_dir, "input17.txt")

ROCKS = \
[
  [[1], [1], [1], [1]],
  [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
  [[0, 0, 1], [0, 0, 1], [1, 1, 1]],
  [[1, 1, 1, 1]],
  [[1, 1], [1, 1]]
]

grid = {}
xy = []

#TARGET = 

#DELAY  = 2934
#LOOP = 10091
#TAIL = 320

H_DELAY = 804
H_LOOP = 2783
#H_TAIL = 0

R_DELAY = 509
R_LOOP = 1745
R_AFTER = 501


def oob(x, y):
  return x < 0 or x > 6 or y < 0

def canmove(rock, dx, dy):
  #print(grid)
  for x in range(len(rock)):
    for y in range(len(rock[0])):
      gx = xy[0] + x + dx
      gy = xy[1] - y + dy
      #print(gx, gy, rock[x][y], (gx, gy) in grid.keys())
      if oob(gx, gy) or (rock[x][y] == 1 and (gx, gy) in grid.keys()):
        #print("  fail", gx, gy)
        return False
  return True

def moveside(rock, dir):
  if canmove(rock, dir, 0):
    xy[0] += dir

def movedown(rock):
  ok = canmove(rock, 0, -1)
  if ok:
    xy[1] -= 1
  return not ok

def freezerock(rock, xy):
  global grid
  for x in range(len(rock)):
    for y in range(len(rock[0])):
      nx = xy[0] + x
      ny = xy[1] - y
      if rock[x][y] == 1:
        grid[(nx, ny)] = True

def printtower(ymax, rows=-1):
  ymin = -1 if rows == -1 else ymax - rows
  for y in range(ymax, ymin, -1):
    line = ""
    for x in range(0, 7):
      if (x, y) in grid:
        line += "#"
      else:
        line += "."
    print(line)

def main():
  global xy
  with open(in_file, 'r') as f:
    blows = ""
    for line in f:
      line = line.rstrip()
      blows = line

    steps = 0
    deltasteps = 0
    placed = 0
    currock = ROCKS[0]
    xy = [2, 2 + len(currock[0])]
    maxy = -1
    maxdelta = -1
    while placed < R_DELAY + 2*R_LOOP + R_AFTER:#steps < DELAY + 2*len(blows) + TAIL:# and placed < 2022:
      b = 1 if blows[steps % len(blows)] == ">" else -1

      #print("start ", steps, xy)
      moveside(currock, b)
      #print("left  " if b == -1 else "right ", xy)
      done = movedown(currock)
      #print("down ", xy)
      if done:
        # print(grid)
        freezerock(currock, xy)
        #print(grid)
        placed += 1
        maxy = max(maxy, xy[1])
        currock = ROCKS[placed % len(ROCKS)]
        #print(currock)
        maxdelta = max(maxdelta, deltasteps)
        if deltasteps > 49:
         print("Freezing ", xy, steps, deltasteps, maxy, placed)
         #printtower(maxy, deltasteps)
        deltasteps = 0
        xy = [2, 3 + len(currock[0]) + maxy]

      steps += 1
      deltasteps += 1
      #print("")
    #print(grid)
    print(steps)
    print("Done ", steps, deltasteps, maxy, placed)
    #print("final")
    #printtower(maxy, 20)


if __name__=="__main__":
  start_time = time.time()
  main()
  print("--- %s seconds ---" % (time.time() - start_time))
