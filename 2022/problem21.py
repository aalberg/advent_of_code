import os

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2022\\"
in_file = os.path.join(in_dir, "test21.txt")

monkeys = {}

class Monkey:
  def __init__(self, name, value, left=None, right=None, op=None):
    self.name = name
    self.value = value
    self.left = left
    self.right = right
    self.op = op

  def eval(self):
    if self.value:
      return self.value
    #print(self.left, self.right, self.value, self.op)

    a = monkeys[self.left].eval()
    b = monkeys[self.right].eval()
    if self.op == "+":
      return a + b
    elif self.op == "-":
      return a - b
    elif self.op == "*":
      return a * b
    elif self.op == "/":
      return int(a / b)
      #return a/b
    #print("bad", self.op)
    return None

  def str_depth(self, depth):
    leftpad = "  " * depth
    if self.value:
      return leftpad + self.name + " " + str(self.value)
    return leftpad + self.name + " " + self.op + "\n" + monkeys[self.left].str_depth(depth + 1) + "\n" + monkeys[self.right].str_depth(depth + 1)

  def path_to_human(self):
    if self.name == "humn":
      return ""

    if self.left:
      l = monkeys[self.left].path_to_human()
      if l != None:
        return "l" + l
    if self.right:
      r = monkeys[self.right].path_to_human()
      if r != None:
        return "r" + r
    return None

  def __str__(self):
    return self.str_depth(0)

def invert_op(op):
  if op == "+":
    return "-"
  elif op == "-":
    return "+"
  elif op == "*":
    return "/"
  elif op == "/":
    return "*"

def main():
  with open(in_file, 'r') as f:
    for line in f:
      line = line.rstrip().split()
      if len(line) == 0:
        break

      line[0] = line[0][:-1]
      if len(line) == 2:
        monkeys[line[0]] = Monkey(line[0], int(line[1]))
      else:
        monkeys[line[0]] = Monkey(line[0], None, line[1], line[3], line[2])

  print(monkeys["root"])
  print(monkeys["root"].eval())
  print(monkeys["root"].path_to_human())

  path = monkeys["root"].path_to_human()
  for i in range(len(path) - 1)
    c = path[i]
    nc = path[i + 1]
    root = monkeys["root"]
    left = monkeys[root.left]
    right = monkeys[root.right]
    if c == "l":
      temp = 
      root.left = 
    else:

  print(monkeys["root"])
  print(monkeys[monkeys["root"].left].eval())
  print(monkeys[monkeys["root"].right].eval())
  



if __name__=="__main__":
  main()
