import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time

PART = 1
TEST = 0
PROBLEM = 9
in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_pattern = "test%d.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)

def main():
  with open(in_file, 'r') as f:
    total1 = 0
    total2 = 0
    for line in f:
      cur = [int(i) for i in line.rstrip().split()]
      h = 0
      while any(c != 0 for c in cur):
        total1 += cur[-1]
        total2 += (1 if h % 2 == 0 else -1) * cur[0]
        cur = [cur[i] - cur[i-1] for i in range(1, len(cur))]
        h += 1

    print(total1)
    print(total2)


if __name__=="__main__":
  main()
