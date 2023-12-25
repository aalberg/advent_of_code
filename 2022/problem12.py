import os
from collections import deque

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2022\\"
in_file = os.path.join(in_dir, "input12.txt")

prios = "abcdefghijklmnopqrstuvwxyz"

def toPrio(s):
  if s == "S":
    return -1
  elif s == "E":
    return -26
  return prios.find(s) + 1

mountain = []

def inbounds(x, y):
  return x >= 0 and x < len(mountain) and y >= 0 and y < len(mountain[0])

def canstep(cur, dest):
  return (mountain[dest[0]][dest[1]] - mountain[cur[0]][cur[1]]) <= 1

def condtostr(ib, cost, height, targetcost, curh, targeth):
  if not ib:
    return ""
  if not height:
    return "height " + str(curh) + " " + str(targeth)
  if not cost:
    return "cost  " + str(targetcost)
  return "adding"

def main():
  with open(in_file, 'r') as f:
    for line in f:
      line = line.rstrip()
      mountain.append([toPrio(h) for h in line])
    # for i in range(len(mountain)):
    #   print(mountain[i])
    q = deque()
    #start = None
    target = None
    costs = [[-1 for i in range(len(mountain[1]))] for j in range(len(mountain))]
    for i in range(len(mountain)):
      for j in range(len(mountain[0])):
        if mountain[i][j] == -1 or mountain[i][j] == 1:
          start = (i, j, 0)
          costs[i][j] = 0
          mountain[i][j] = 1
          q.append(start)
        elif mountain[i][j] == -26:
          target = (i, j)
          mountain[i][j] = 26
    #print(start)
    print([k for k in q])
    print(target)

    # q.append(start)
    count = 0
    last = 0
    while len(q) > 0:
      e = q.popleft()
      #costs[e[0]][e[1]] = e[2]
      if e[0] == target[0] and e[1] == target[1]:
        print("Done:", e[2])
        last = e[2]
        #break
      for i in range(4):
        sign = -1 if i < 2 else 1
        dx = sign if i % 2 == 0 else 0
        dy = sign if i % 2 == 1 else 0
        nxy = tuple((e[0] + dx, e[1] + dy, e[2] + 1))

        # debug
        # ib = inbounds(nxy[0], nxy[1])
        # cond = True
        # if ib:
        #   cost = costs[nxy[0]][nxy[1]] == -1
        #   height = canstep(e, nxy)
        #   cond = ib and cost and height
        #   #print(e, nxy, condtostr(ib, cost, height, costs[nxy[0]][nxy[1]], mountain[e[0]][e[1]], mountain[nxy[0]][nxy[1]]))
        # else:
        #   cond = False
        #   #print(e, nxy, "oob")

        if inbounds(nxy[0], nxy[1]) and costs[nxy[0]][nxy[1]] == -1 and canstep(e, nxy):
        #if cond:
          costs[nxy[0]][nxy[1]] = nxy[2]
          q.append(nxy)
          #print("  ", nxy)
      count += 1
      # if count % 1000 == 0:
      #   print(count)
      #   for i in range(len(mountain)):
      #     print(costs[i])
    print("")
    for i in range(len(mountain)):
      print(costs[i])
    print(last)

if __name__=="__main__":
  main()
