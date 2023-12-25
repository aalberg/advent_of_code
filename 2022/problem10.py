import os
import math

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2022\\"
in_file = os.path.join(in_dir, "input10.txt")

def shouldsample(cycle):
  mod40 = (cycle - 20) % 40
  return mod40 == 0

image = [["." for i in range(40)] for j in range(6)]

def visible(cycle, x):
  return abs(x - cycle) <= 1

def draw(cycle, x):
  drawx = cycle % 40
  drawy = int(cycle / 40)
  if visible(drawx, x):
    image[drawy][drawx] = "#"

def main():
  with open(in_file, 'r') as f:
    cycle = 0
    p = 1
    x = 1
    strength = 0

    for line in f:
      line = line.rstrip().split()

      # if len(line) == 1:
      #   if shouldsample(cycle):
      #     print("-------", cycle, cycle * x)
      #     strength += cycle * x
      #   cycle += 1
      # elif len(line) > 1:
      #   p = x
      #   x += int(line[1])
      #   cycle += 2
      #   for c in range(cycle - 2, cycle):
      #     if shouldsample(c):
      #       print("-------", c, c * p)
      #       strength += c * p
      #print(cycle, x, p)
      if len(line) == 1:
        draw(cycle, x)
        cycle += 1
      elif len(line) > 1:
        d = int(line[1])
        draw(cycle, x)
        cycle += 1
        draw(cycle, x)
        cycle += 1
        x += d


    #print(strength)
    for line in image:
      print("".join(line))





if __name__=="__main__":
  main()
