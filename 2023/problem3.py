import os
from collections import defaultdict 

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_file = os.path.join(in_dir, "input3.txt")

nums = "0123456789"
grid = []

def def_value():
  return []
gears = defaultdict(def_value)

def inbounds(x, y):
  return x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)

def is_num(c):
  return nums.find(c) >= 0

def is_symbol(c):
  return not c == "." and not is_num(c)

def is_near_symbol(x1, x2, y):
  for xc in range(x1 - 1, x2 + 1):
    for yc in range(y - 1, y + 2):
      if inbounds(xc, yc) and is_symbol(grid[yc][xc]):
        #print("ins", xc, yc, "input", x1, x2, y)
        return True

def get_gears_near(x1, x2, y):
  gears = []
  for xc in range(x1 - 1, x2 + 1):
    for yc in range(y - 1, y + 2):
      if inbounds(xc, yc) and is_symbol(grid[yc][xc]) and grid[yc][xc] == "*":
        gears.append((xc, yc))
  return gears

def main():
  with open(in_file, 'r') as f:
    for line in f:
      line = line.rstrip()
      grid.append(line)

  total = 0
  for y in range(len(grid)):
    x = 0
    while x < len(grid[0]):
      if is_num(grid[y][x]):
        end = x
        while end < len(grid[0]) and is_num(grid[y][end]):
          end += 1
        val = int(grid[y][x:end])
        if is_near_symbol(x, end, y):
          total += val
          gears_near = get_gears_near(x, end, y)
          for g in gears_near:
            gears[g].append(val)
        x = end + 1
      else:
        x += 1
  print("sum:", total)

  gear_sum = 0
  for gear, pns in gears.items():
    if len(pns) == 2:
      gear_sum += pns[0] * pns[1]
  print("gear_sum", gear_sum)

if __name__=="__main__":
  main()
