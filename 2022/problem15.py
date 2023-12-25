import os
import re
import time

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2022\\"
filepath = "input15.txt"
in_file = os.path.join(in_dir, filepath)

restring = r"[^-0-9)]*([-0-9)]+)[^-0-9)]*([-0-9]+)[^-0-9)]*([-0-9]+)[^-0-9)]*([-0-9]+)[^-0-9)]*"
pattern = re.compile(restring)

TESTROW = 10 if filepath.startswith("test") else 2000000
TESTMAX = 20 if filepath.startswith("test") else 4000000
#row = {}
sensors = {}
allcandidates = {}

def radius(s, b):
  return abs(s[0] - b[0]) + abs(s[1] - b[1])

def coverrow(sx, sy, bx, by):
  #print(sx, sy, bx, by)
  r = radius((sx, sy), (bx, by))
  height = abs(sy - TESTROW)
  dxmax = r - height
  #print(r, height, dxmax)
  if by == TESTROW:
    row[bx] = False
  for dx in range(-dxmax, dxmax + 1):
    nx = sx + dx
    if nx not in row.keys():
      row[sx + dx] = True
    #print(sx + dx)
  #print("")

def inbounds(x, y):
  return x >= 0 and x <= TESTMAX and y >= 0 and y <= TESTMAX

def toclose(s, b, r):
  return radius(s, b) <= r

def getcandidates(sx, sy, bx, by):
  r = radius((sx, sy), (bx, by)) + 1
  #candidates = {}
  print(sx, sy, bx, by, r)
  for height in range(0, r + 1):
    dx = r - height
    #print(r, height, dx)
    yield (sx + dx, sy + height)
    yield (sx - dx, sy + height)
    yield (sx + dx, sy - height)
    yield (sx - dx, sy - height)
    #candidates[(sx + dx, sy + height)] = True
    #candidates[(sx - dx, sy + height)] = True
    #candidates[(sx + dx, sy - height)] = True
    #candidates[(sx - dx, sy - height)] = True
  #return candidates, r - 1
  #print(candidates.keys())

def main():
  with open(in_file, 'r') as f:
    for line in f:
      line = line.rstrip()
      result = [int(i) for i in pattern.findall(line)[0]]
      #coverrow(result[0], result[1], result[2], result[3])
      
      sensor = (result[0], result[1])
      r = radius((result[0], result[1]), (result[2], result[3]))
      for c in list(allcandidates.keys()):
        if toclose(sensor, c, r + 1):
          del allcandidates[c]

      for c in getcandidates(result[0], result[1], result[2], result[3]):
        if not inbounds(c[0], c[1]):
          continue
        ok = True
        for s, r2 in sensors.items():
          if toclose(s, c, r2):
            ok = False
            break
        if ok:
          allcandidates[c] = True
      sensors[sensor] = r
    print(allcandidates)
    #print(len(row.keys()))
    #print(sorted(row.keys()))
    #print(row)
    #print(sum(1 if row[k] else 0 for k in row.keys()))


if __name__=="__main__":
  start_time = time.time()
  main()
  print("--- %s seconds ---" % (time.time() - start_time))
