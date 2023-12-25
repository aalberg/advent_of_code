import os

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2022\\"
in_file = os.path.join(in_dir, "input2.txt")

themstr = "ABC"
usstr = "XYZ"

def resultPoints(them, us):
  diff = (themstr.find(them) - usstr.find(us)) % 3
  #print(diff)
  if (diff == 0):
    return 3
  if (diff == 1):
    return 0
  if (diff == 2):
    return 6
  return 10000

def playPoints(us):
  if us == "X":
    return 1
  elif us == "Y":
    return 2
  elif us == "Z":
    return 3
  return 1000

def points2(them, result):
  them_index = themstr.find(them)
  result_index = usstr.find(result)
  us_index = (them_index + result_index - 1) % 3
  rp = 3 * usstr.find(result)
  #print(us_index + 1, rp)
  return us_index + 1 + rp

def main():
  with open(in_file, 'r') as f:
    score = 0
    for line in f:
      line = line.rstrip().split()
      #s = resultPoints(line[0], line[1]) + playPoints(line[1])
      s = points2(line[0], line[1])
      score += s
      #print(score, s)
    print(score)


if __name__=="__main__":
  main()