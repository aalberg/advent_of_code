import os

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2022\\"
in_file = os.path.join(in_dir, "input7.txt")

FS_SIZE = 70000000
SPACE_NEEDED = 30000000

class Directory:
  def __init__(self, name, parent = None):
    self.name = name
    self.parent = parent
    self.files = {}
    self.dirs = {}
    self.totalsize = 0

  def move_or_add(self, dirname):
    if dirname in self.dirs.keys():
      return self.dirs[dirname]
    self.dirs[dirname] = Directory(dirname, self)
    return self.dirs[dirname]

  def add_dir(self, dirname):
    self.dirs[dirname] = Directory(dirname, self)

  def add_file(self, filename, size):
    self.files[filename] = size

  def compute_sizes(self):
    self.totalsize = 0
    for size in self.files.values():
      self.totalsize += size
    for child in self.dirs.values():
      self.totalsize += child.compute_sizes()
    return self.totalsize

  def sum_size_under(self, m):
    total = 0
    if self.totalsize <= m:
      total += self.totalsize
    for child in self.dirs.values():
      total += child.sum_size_under(m)
    return total

  def smallest_at_least(self, s):
    cur = FS_SIZE
    if self.totalsize > s:
      cur = self.totalsize
    for child in self.dirs.values():
      cur = min(cur, child.smallest_at_least(s))
    return cur

  def print(self, depth):
    indent = " " * (depth * 2)
    output = indent + self.name  + " " + str(self.totalsize) + "\n"
    for filename, size in self.files.items():
      output += indent + "  " + filename + " " + str(size) + "\n"
    for child in self.dirs.values():
      output += child.print(depth + 1)
    return output

  def __str__(self):
    return self.print(0)

def nextline(f):
  line = f.readline()
  if not line:
    #print("DONE")
    return line
  line = line.rstrip().split()
  #print(line)
  return line

def main():
  with open(in_file, 'r') as f:
    root = Directory("/")
    cur = root
    line = nextline(f) # skip first line, we know it sets us to root.
    line = nextline(f)
    while line:
      command = line[1]
      
      if command == "ls":
        line = nextline(f)
        while line and line[0] != "$":
          if line[0] == "dir":
            cur.add_dir(line[1])
          else:
            cur.add_file(line[1], int(line[0]))
          line = nextline(f)
      elif command == "cd":
        targetdir = line[2]
        if targetdir == "/":
          cur = root
        elif targetdir == "..":
          cur = cur.parent
        else:
          cur = cur.move_or_add(targetdir)
        line = nextline(f)
      else:
        print("BADBAD")
        exit(1)
    root.compute_sizes()
    print(root)
    print(root.sum_size_under(100000))
    print(root.totalsize + SPACE_NEEDED - FS_SIZE)
    print(root.smallest_at_least(root.totalsize + SPACE_NEEDED - FS_SIZE))


if __name__=="__main__":
  main()
