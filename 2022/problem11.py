import os
import math

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2022\\"
filename = "input11.txt"
in_file = os.path.join(in_dir, filename)

monkeys = []

MOD_TEST = 96577
MOD_REAL = 9699690

hardcode_ops_test = [lambda x: x*19,
                     lambda x: x+6,
                     lambda x: x*x,
                     lambda x: x+3]

hardcode_ops_real = [lambda x: x*13,
                     lambda x: x+2,
                     lambda x: x+8,
                     lambda x: x+1,
                     lambda x: x*17,
                     lambda x: x+3,
                     lambda x: x*x,
                     lambda x: x+6]

hardcode_ops = hardcode_ops_test if filename.startswith("test") else hardcode_ops_real
MOD = MOD_TEST if filename.startswith("test") else MOD_REAL

class Monkey:
  def __init__(self, start_items, op, test, throwtrue, throwfalse):
    self.items = start_items
    self.op = op
    self.test = test
    self.throwtrue = throwtrue
    self.throwfalse = throwfalse
    self.inspect_count = 0

  def clearitems(self):
    self.items = []

  def additem(self, item):
    self.items.append(item)

  def throw(self):
    dests = {self.throwtrue: [], self.throwfalse: []}
    for item in self.items:
      self.inspect_count += 1
      newvalue = int(self.op(item) % MOD)
      dest = self.throwtrue if newvalue % self.test == 0 else self.throwfalse
      dests[dest].append(newvalue)
      #print(dest, item, newvalue)
    return dests

  def count(self):
    return self.inspect_count

  def __str__(self):
    return " ".join([str(self.items), str(self.inspect_count)])#, str(self.test), str(self.throwtrue), str(self.throwfalse), str(self.inspect_count)])

def nextline(f):
  line = f.readline()
  if not line:
    return line
  line = line.rstrip()
  #print(line)
  return line

def parsemonkey(f):
  line = nextline(f)
  items = [int(i) for i in line.split(":")[1].lstrip().split(",")]
  nextline(f)  # Skip this line
  op = hardcode_ops[len(monkeys)]
  testnum = int(nextline(f).split()[-1])
  throwtrue = int(nextline(f).split()[-1])
  throwfalse = int(nextline(f).split()[-1])
  monkeys.append(Monkey(items, op, testnum, throwtrue, throwfalse))
  #print([str(m) for m in monkeys])

def main():
  with open(in_file, 'r') as f:
    for line in f:
      line = line.rstrip()
      if line.startswith("Monkey"):
        parsemonkey(f)
    #print([str(m) for m in monkeys])
    for i in range(10000):
      targets = {i : [] for i in range(len(monkeys))}
      for m in monkeys:
        t = m.throw()
        m.clearitems()
        for m, il in t.items():
          for i in il:
            monkeys[m].additem(i)
      #     targets[m].extend(il)
      # for m in monkeys:
      #   m.clearitems()
      # print(targets)
      # for m, il in targets.items():
      #   for i in il:
      #     monkeys[m].additem(i)

      #for m in monkeys:
      #  print(str(m))
      #print([str(m) for m in monkeys])
    counts = [m.inspect_count for m in monkeys]
    print(counts)
    counts = sorted(counts)
    print(counts[-1] * counts[-2])

if __name__=="__main__":
  main()
