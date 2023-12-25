import os

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2022\\"
in_file = os.path.join(in_dir, "input4.txt")

def toRange(text_range):
  s = text_range.split("-")
  return (int(s[0]), int(s[1]))

def contains(big, small):
  return big[0] <= small[0] and big[1] >= small[1]

def containsSingle(r, v):
  return v >= r[0] and v <= r[1]

def overlaps(r1, r2):
  return containsSingle(r1, r2[0]) or containsSingle(r1, r2[1]) \
      or containsSingle(r2, r1[0]) or containsSingle(r2, r1[1])

def main():
  with open(in_file, 'r') as f:
    count = 0
    for line in f:
      line = line.rstrip().split(',')
      r1 = toRange(line[0])
      r2 = toRange(line[1])
      # if contains(r1, r2) or contains(r2, r1):
      if overlaps(r1, r2):
         count += 1
      print(r1, r2, count)
    print(count)


if __name__=="__main__":
  main()