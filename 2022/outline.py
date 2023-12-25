import os

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2022\\"
in_file = os.path.join(in_dir, "test19.txt")

monkeys = {}

def Monkey:
  def __init__(self, value, left=None, right=None, op=None):
    self.value = value
    self.left = left
    self.left = right
    self.op = op

  def eval(self):
    if self.value:
      return self.value
    a = monkeys[self.left].eval()
    b = monkeys[self.right].eval()
    if self.op == "+":
      return a + b
    elif self.op == "-":
      return a - b
    elif self.op == "*":
      return a * b
    elif self.op == "*":
      return a / b
    return None


def main():
  with open(in_file, 'r') as f:
    for line in f:
      line = line.rstrip().split()
      if len(line) == 0:
        break
      elif len(line) == 2:
        monkeys[line[0][-1]] = Monkey(int(line[1]))
      else:
        monkeys[line[0][-1]] = Monkey(None, line[1], line[3], line[2])
  print(monkeys["root"].eval())

if __name__=="__main__":
  main()
