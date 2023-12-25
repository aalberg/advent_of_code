import os

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2022\\"
in_file = os.path.join(in_dir, "input8.txt")

trees = []

def inbounds(x, y):
  return x >= 0 and x < len(trees) and y >= 0 and y < len(trees[0])

def getscore(x, y):
  score = 1
  for i in range(4):
    nx = x
    ny = y
    sign = -1 if i < 2 else 1
    dx = sign if i % 2 == 0 else 0
    dy = sign if i % 2 == 1 else 0
    dirscore = 0
    while True:
      nx += dx
      ny += dy
      if not inbounds(nx, ny):
        break
      elif trees[x][y] <= trees[nx][ny]:
        dirscore += 1
        break
      dirscore += 1
    if dirscore == 0:
      return 0
    score *= dirscore
  return score

def main():
  with open(in_file, 'r') as f:
    for line in f:
      line = line.rstrip()
      if len(line) == 0:
        break
      trees.append([int(c) for c in line])
    print(trees)

    # visible = [[False for y in range(len(trees[0]))] for x in range(len(trees))]
    # for x in range(len(trees)):
    #   maxu = -1
    #   maxd = -1
    #   maxl = -1
    #   maxr = -1
    #   for y in range(len(trees[0])):
    #     rx = len(trees) - 1 - x
    #     ry = len(trees[0]) - 1 - y
        
    #     if trees[x][y] > maxl:
    #       visible[x][y] = True
    #       maxl = trees[x][y]

    #     if trees[y][x] > maxu:
    #       visible[y][x] = True
    #       maxu = trees[y][x]

        
    #     if trees[rx][ry] > maxr:
    #       visible[rx][ry] = True
    #       maxr = trees[rx][ry]

    #     if trees[ry][rx] > maxd:
    #       visible[ry][rx] = True
    #       maxd = trees[ry][rx]
    # print(visible)

    # count = 0
    # for x in range(len(trees)):
    #   for y in range(len(trees[0])):
    #     if (visible[x][y]):
    #       count += 1
    # print(count)

    scores = [[0 for y in range(len(trees[0]))] for x in range(len(trees))]
    maxscore = 0
    for x in range(len(trees)):
      for y in range(len(trees[0])):
        scores[x][y] = getscore(x, y)
        maxscore = max(scores[x][y], maxscore)
        #for d in range(1, len(trees)):
    print(scores)
    print(maxscore)

if __name__=="__main__":
  main()
