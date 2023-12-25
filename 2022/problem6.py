import os

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2022\\"
in_file = os.path.join(in_dir, "input6.txt")

L = 14

def ismarker(s):
  #print(s)
  m = {}
  for c in s:
    if c in m.keys():
      return False
    m[c] = True
  return True

def main():
  with open(in_file, 'r') as f:
    count = 0
    for line in f:
      line = line.rstrip()
      for i in range(len(line) - L + 1):
        if ismarker(line[i:i + L]):
          print(i + L, line[i:i + L])


if __name__=="__main__":
  main()
