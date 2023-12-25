import os

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2022\\"
in_file = os.path.join(in_dir, "input1.txt")

def update_max(max_cal, cur):
  #print(max_cal, cur)
  for i in range(3):
    if cur > max_cal[i]:
      max_cal.insert(i, cur)
      break;
  return max_cal[0:3]

def main():
  with open(in_file, 'r') as f:
    max_cal = [0, 0, 0]
    cur = 0
    for line in f:
      line = line.rstrip()
      if len(line) > 0:
        cur += int(line)
      else:
        max_cal = update_max(max_cal, cur)
        cur = 0
    max_cal = update_max(max_cal, cur)
    print(max_cal)
    print(sum(max_cal))


if __name__=="__main__":
  main()