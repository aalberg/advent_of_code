import os
import math

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_file = os.path.join(in_dir, "input6_2.txt")

nums = "0123456789"

def main():
  times = []
  distances = []
  with open(in_file, 'r') as f:
    for i, line in enumerate(f):
      line = [int(i) for i in filter(None, line.rstrip().split(":")[1].split())]
      if i == 0:
        times = line
      else:
        distances = line
      
  total = 1
  for i in range(len(times)):
    t = times[i]
    d_target = distances[i] + .0000001

    det = t*t - 4*d_target
    t1 = (t - math.sqrt(det))/2
    t2 = (t + math.sqrt(det))/2
    
    ways = math.floor(t2) - math.ceil(t1) + 1
    print(d_target, t, t1, t2, math.ceil(t1), math.floor(t2), ways)
    total *= ways
  print("total:", total)
      

if __name__=="__main__":
  main()
