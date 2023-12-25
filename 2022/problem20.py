import os

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2022\\"
in_file = os.path.join(in_dir, "input20.txt")

KEY = 811589153

class Node:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def __str__(self):
    return str(self.value)

  def __repr__(self):
    return "|" + str(self.prev) + ", " + str(self.value) + ", " + str(self.next) + "|"


def printlist(start, maxsize):
  outstr = [str(start)]
  cur = start.next
  while cur != start:
    outstr.append(str(cur))
    cur = cur.next
    if not cur:
      print("BAD")
      return
    if len(outstr) > maxsize:
      break
  print(", ".join(outstr))
  if len(outstr) > maxsize:
    print("BADBADBAD")


def find_zero(node):
  cur = node
  while True:
    if cur.value == 0:
      return cur
    cur = cur.next


def find_index_from(node, index):
  cur = node
  for i in range(index):
    cur = cur.next
  return cur.value


def main():
  nodes = {}
  root = Node(None)
  cur = root
  with open(in_file, 'r') as f:
    for i, line in enumerate(f):
      line = line.rstrip()
      cur.next = Node(int(line) * 811589153, cur, None)
      cur = cur.next
      nodes[i] = cur

  root = root.next
  root.prev = cur
  cur.next = root

  zero = find_zero(root)
  #printlist(zero, len(nodes))
  for j in range(10):
    for i in range(len(nodes)):
    #for i in range(1):
      start = nodes[i]
      move = start.value % (len(nodes) - 1)
      if move == 0:
        #print("skip", move)
        continue

      cur = nodes[i]
      first = None
      second = None
      #print("processing", move)
      if move > 0:
        for i in range(move):
          cur = cur.next
        first = cur
        second = cur.next
      elif move < 0:
        for i in range(-move):
          cur = cur.prev
        first = cur.prev
        second = cur

      # Remove start from where it was
      start.prev.next = start.next
      start.next.prev = start.prev

      # Insert start between first and second
      start.prev = first
      start.next = second
      first.next = start
      second.prev = start

      #printlist(zero, len(nodes))

  
  #printlist(zero, len(nodes))
  tofind = [1000, 2000, 3000, len(nodes)]
  total = 0
  for i in tofind:
    value = find_index_from(zero, i)
    total += value
    print(i, value)
  print(total)

if __name__=="__main__":
  main()
