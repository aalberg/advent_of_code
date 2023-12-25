import os
import re

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2022\\"
in_file = os.path.join(in_dir, "input5.txt")

def main():
  with open(in_file, 'r') as f:
    initialstacks = []
    while line := f.readline():
      line = line.rstrip()
      if len(line) == 0:
        break
      initialstacks.append(line)
    #print(initialstacks)

    count = int(initialstacks.pop().split()[-1])
    stacks = []
    for i in range(count):
      stacks.append([])

    #print(initialstacks)
    #print(stacks)
    for row in reversed(initialstacks):
      starts = re.finditer("\[", row)
      for start in starts:
        index = int(start.start(0))
        value = row[index + 1]
        stack_num = int(index / 4)
        stacks[stack_num].append(value)

    print(stacks)

    for line in f:
      line = line.rstrip().split()
      c = int(line[1])
      stack_from = int(line[3]) - 1
      stack_to = int(line[5]) - 1

      # for i in range(c):
      #   n = stacks[stack_from].pop()
      #   stacks[stack_to].append(n)
      stacks[stack_to].extend(stacks[stack_from][-c:])
      del stacks[stack_from][-c:]
      #print(stacks)

    outstr = ""
    for s in stacks:
      outstr += s[-1]
    #print(stacks)
    print(outstr)

if __name__=="__main__":
  main()