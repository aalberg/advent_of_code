import os

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_file = os.path.join(in_dir, "input2.txt")

def main():
  with open(in_file, 'r') as f:
    total = 0
    for i, line in enumerate(f):
      if len(line) <= 1:
        break
      line = line.rstrip().split(": ")[1]
      rounds = line.split("; ")
      valid = True
      for r in rounds:
        available = {"red": 12, "green": 13, "blue": 14}
        sets = r.split(", ")
        for s in sets:
          num, color = s.split(" ")
          num = int(num)
          available[color] -= num
          #print(num, color)
        #print(available)
        for _, v in available.items():
          if v < 0:
            valid = False
        if not valid:
          break
      #print(valid, line)

      if valid:
        total += i + 1
    print("sum", total)

def main2():
  with open(in_file, 'r') as f:
    total = 0
    for i, line in enumerate(f):
      if len(line) <= 1:
        break
      line = line.rstrip().split(": ")[1]
      rounds = line.split("; ")
      valid = True
      max_needed = {"red": 0, "green": 0, "blue": 0}
      for r in rounds:
        needed = {"red": 0, "green": 0, "blue": 0}
        sets = r.split(", ")
        for s in sets:
          num, color = s.split(" ")
          num = int(num)
          needed[color] += num
        #print(needed)
        for c, v in needed.items():
          max_needed[c] = max(max_needed[c], v)
        #print(max_needed)
      power = 1
      for _, v in max_needed.items():
        power *= v
      total += power
      #print(power)
    print("sum", total)

if __name__=="__main__":
  main2()
