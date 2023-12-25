import os
import math

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2022\\"
in_file = os.path.join(in_dir, "input9.txt")

L = 10

def dirtotuple(d):
  key = "LURD"
  i = key.find(d)
  sign = -1 if i < 2 else 1
  return (sign if i % 2 == 0 else 0, sign if i % 2 == 1 else 0)


def movetail(xy, txy):
  dx = xy[0] - txy[0]
  dy = xy[1] - txy[1]
  if abs(dx) <= 1 and abs(dy) <= 1:
    return txy

  nx = 0 if dx == 0 else math.copysign(1, dx)
  ny = 0 if dy == 0 else math.copysign(1, dy)
  return [int(txy[0] + nx), int(txy[1] + ny)]

def main():
  with open(in_file, 'r') as f:
    visited = {}
    xy = [[0, 0] for i in range(L)]
    #print(xy)
    for line in f:
      line = line.rstrip().split()
      d = line[0]
      count = int(line[1])

      dxy = dirtotuple(d)
      #print(line, dxy)
      for i in range(count):
        for j in range(2):
          xy[0][j] += dxy[j]
        for j in range(1, len(xy)):
          xy[j] = movetail(xy[j-1], xy[j])
        # for j in range(len(txy)):
        #   txy = movetail(xy, txy)
        #print(xy)
        visited[tuple(xy[L - 1])] = True
    #print(visited.keys())
    print(len(visited.keys()))



if __name__=="__main__":
  main()
