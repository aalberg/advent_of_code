import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time

PART = 1
TEST = 0
PROBLEM = 19
in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_pattern = "test%d.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)
NUMS = "0123456789"

class Condition:
  def __init__(self, cond_str):
    if "<" in cond_str:
      cond = cond_str.split("<")
      self.var = cond[0]
      self.less = True
      self.val = int(cond[1])
    elif ">" in cond_str:
      cond = cond_str.split(">")
      self.var = cond[0]
      self.less = False
      self.val = int(cond[1])
    else:
      print("BADBABD", cond_str)

  def eval(self, part):
    if self.less:
      return part[self.var] < self.val
    return part[self.var] > self.val

  def eval_range(self, r):
    tvr = r.vars[self.var]
    if self.less:
      if tvr[1] < self.val:
        return r, None
      elif tvr[0] >= self.val:
        return None, r
      r1 = r.copy()
      r2 = r.copy()
      r1.vars[self.var][1] = self.val - 1
      r2.vars[self.var][0] = self.val
      return r1, r2
    if tvr[0] > self.val:
      return r, None
    elif tvr[1] <= self.val:
      return None, r
    r1 = r.copy()
    r2 = r.copy()
    r1.vars[self.var][0] = self.val + 1
    r2.vars[self.var][1] = self.val
    return r1, r2

  def __repr__(self):
    return str(self)

  def __str__(self):
    return self.var + " " + str(self.less) + " " + str(self.val)

class PartRange():
  RANGE_MAX = 4000
  def __init__(self):
    self.vars = {}
    self.vars["x"] = [1, PartRange.RANGE_MAX]
    self.vars["m"] = [1, PartRange.RANGE_MAX]
    self.vars["a"] = [1, PartRange.RANGE_MAX]
    self.vars["s"] = [1, PartRange.RANGE_MAX]

  def copy(self):
    new_range = PartRange()
    new_range.vars["x"] = list(self.vars["x"])
    new_range.vars["m"] = list(self.vars["m"])
    new_range.vars["a"] = list(self.vars["a"])
    new_range.vars["s"] = list(self.vars["s"])
    return new_range

  def __repr__(self):
    return str(self)

  def __str__(self):
    return "pl" + str(self.vars)

workflows = defaultdict(list)

def process_part(part):
  cur = "in"
  i = 0
  while i < 10:
    s = workflows[cur]
    dest = s[-1]
    for cond, d in s[:-1]:
      #print("try", cond)
      if cond.eval(part):
        dest = d
        break

    #print("to", dest)
    cur = dest
    if cur == "R":
      return False
    elif cur == "A":
      return True
    i += 1
  exit(1)

def process_part_range():
  cur = defaultdict(list)
  cur["in"] = [PartRange()]
  i = 0
  overall_accepted = []
  while i < 10:
    #print("---------")
    #print(cur)
    next_state = defaultdict(list)
    for state, range_list in cur.items():
      workflow = workflows[state]
      #print("workflow", state, workflow)
      for r in range_list:
        #print("  range", range_list)
        r_to_try = r
        for cond, new_dest in workflow[:-1]:
          # print("    r_to_try", r_to_try)
          # print("    cond", cond)
          # print("    dest", new_dest)
          meets, rem = cond.eval_range(r_to_try)
          # print("      a", meets)
          # print("      r", rem)
          if meets != None:
            if new_dest == "A":
              #print("      accepted parts", meets)
              overall_accepted.append(meets)
            elif new_dest != "R":
              #print("      to", new_dest, meets)
              next_state[new_dest].append(meets)
          r_to_try = rem
          if r_to_try == None:
            break
        if r_to_try != None:
          default_dest = workflow[-1]
          if default_dest == "A":
            #print("    accepted default", r_to_try)
            overall_accepted.append(r_to_try)
          elif default_dest != "R":
            #print("    to default", default_dest, r_to_try)
            next_state[default_dest].append(r_to_try)

      #print("next_state", next_state)
    cur = next_state
    if len(cur.keys()) == 0:
      break
    i += 1
  if i >= 10:
    print("BADBADBAD", cur)
  #print("overall_accepted", overall_accepted)
  total_parts = 0
  for a in overall_accepted:
    partial = 1
    for _, v in a.vars.items():
      partial *= (v[1] - v[0] + 1)
    # print(a, partial)
    total_parts += partial
  print("total_parts", total_parts)

def main():
  ratings = []
  with open(in_file, 'r') as f:
    mode = False
    for line in f:
      line = line.rstrip()
      if len(line) == 0:
        mode = True
        continue

      if not mode:
        name, flow = line.split("{")
        flow = flow[:-1].split(",")
        for f in flow:
          if ":" in f:
            cond, target = f.split(":")
            workflows[name].append((Condition(cond), target))
          else:
            workflows[name].append(f)
      else:
        rating = line[1:-1].split(",")
        part = {}
        for r in rating:
          rs = r.split("=")
          part[rs[0]] = int(rs[1])
        ratings.append(part)
  # print("----")
  # for n, w in workflows.items():
  #   print(n, w)
  total = 0
  for i, r in enumerate(ratings):
    #print(i, r)
    a = process_part(r)
    #print(a)
    if a:
      total += sum(r.values())
  print(total)

  process_part_range()

if __name__=="__main__":
  main()
