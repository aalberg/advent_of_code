import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import re
import time

PART = 1
TEST = 0
PROBLEM = 17
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
IN_PATTERN = "test2.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"

def nextline(f):
  line = f.readline()
  if not line:
    return ""
  line = line.rstrip()
  return line

def combo(o, a, b, c):
  if o < 4:
    return o
  if o == 4:
    return a
  if o == 5:
    return b
  if o == 6:
    return c
  raise ValueError

def run_sim(a, b, c, p):
  output = []
  i = 0
  steps = 0

  while True:
    steps += 1
    print(i, hex(a), hex(b), hex(c), sep='\t')
    if not 0 <= i < len(p):
      print("halting")
      break
    o = p[i+1]
    if p[i] == 0:
      a = a // (2**combo(o, a, b, c))
    elif p[i] == 1:
      b = b ^ o
    elif p[i] == 2:
      b = combo(o, a, b, c) % 8
    elif p[i] == 3:
      if a != 0:
        i = o
        continue
    elif p[i] == 4:
      b = b ^ c
    elif p[i] == 5:
      output.append(str(combo(o, a, b, c) % 8))
    elif p[i] == 6:
      b = a // (2**combo(o, a, b, c))
    elif p[i] == 7:
      c = a // (2**combo(o, a, b, c))
    i += 2
  print("steps: ", steps)
  print(",".join(output))
  return output

def static_analysis(p):
  bins = [0] * 8
  for i, c in enumerate(p):
    if i % 2 == 0:
      bins[c] += 1
      if c == 0:
        print("adv: ", i, p[i+1])
      if c == 1:
        print("bxl: ", i, p[i+1])
      if c == 2:
        print("bst: ", i, p[i+1])
      if c == 3:
        print("jump: ", i)
      if c == 4:
        print("bxc: ", i)
      if c == 5:
        print("out: ", i, p[i+1])
      if c == 6:
        print("bdv: ", i, p[i+1])
      if c == 7:
        print("cdv: ", i, p[i+1])
  print(bins)

def simplified_sim(a):
  b = 0
  c = 0
  output = []

  while a > 0:
    b = a % 8
    b = b ^ 3
    c = a // 2**b
    a = a // 8
    b = b ^ c
    b = b ^ 5
    output.append(b % 8)
  #print(",".join([str(i) for i in output]))
  return output

def find_a_single(target):
  for a in range(9):
    output = simplified_sim(a)
    #print(output)
    if len(output) == 1 and output[0] == target:
      print("hi", a)
      return a
    elif len(output) > 1:
      print("badbad")
  return None

def solve(p):
  overall_a = 0
  for o in reversed(p):
    a = find_a_single(o)
    if a is None:
      print("BADBAD", o)
      exit()
    overall_a = overall_a * 8 + a
    print(overall_a)
  return overall_a

def solve2(program):
  cur_programs = deque()
  cur_programs.append((0, []))
  while len(cur_programs) > 0:
    p = cur_programs.popleft()
    start = len(program) - len(p[1])
    if start < 0:
      continue
    possible = []
    for i in range(1, 4096):
      out = simplified_sim(i)
      start2 = len(program) - len(p[1]) - len(out)
      if start2 < 0:
        continue
      ok = True
      for j, c in enumerate(out):
        if program[start2 + j] != c:
          ok = False
      if ok:
        print(p, i, out)
        possible.append((i, out))
        out.extend(p[1])
        cur_programs.append((p[0] * 8**len(out) + i, out))


def list_match(a, b):
  for i, sa in enumerate(a):
    if sa != b[i]:
      return False
  return True

def main():
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    a = int(nextline(f).replace("Register A: ", ""))
    b = int(nextline(f).replace("Register B: ", ""))
    c = int(nextline(f).replace("Register C: ", ""))
    _ = nextline(f)
    p = [int(i) for i in nextline(f).replace("Program: ", "").split(",")]

    print(a, b, c, p)
    #static_analysis(p)
    #run_sim(a, b, c, p)
    simplified_sim(a)
    #find_a_single(p[-1])
    print("-----------")
    # for asdf in range(8):
    #   print(asdf, simplified_sim(asdf))
    print("-----------")
    #solved_a = solve(p)
    #solve2(p)
    print("-----------")
    #print(len(simplified_sim(8**16-1)))

    d = {
      0: 6,
      1: 7,
      2: 4,
      3: 5,
      4: 0,
      5: 2,
      6: 3,
      7: 1,
    }
    cur_as = set()
    cur_as.add(0)
    solutions = []
    for o in reversed(p):
      new_as = set()
      for cur_a in cur_as:
        for i in range(8):
          test_a = cur_a * 8 + i
          out = simplified_sim(test_a)

          if list_match(out, p[len(p)-len(out):]):
            if (len(p) == len(out)):
              print("DONE: ", test_a)
              solutions.append(test_a)
            new_as.add(test_a)
            print(cur_a, i, simplified_sim(test_a))
      cur_as = new_as
    print(sorted(solutions))


# a in range 8**15 8**16-1

# bst:  b = a % 8
# bxl:  b = b ^ 3
# cdv:  c = a // 2**b
# adv:  a = a // 8
# bxc:  b = b ^ c
# bxl:  b = b ^ 5
# out:  b % 8
# jump: 0


#
# b odd, c even, or vice versa
# 1
# 4

if __name__ == "__main__":
  main()

# 0x1CAC0
#   3   4   5   3   0   0
#0b11 100 101 011 000 000
# 117440 0 0 [0, 3, 5, 4, 3, 0]

# 0x1586AA0
