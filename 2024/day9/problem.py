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
PROBLEM = 9
IN_DIR = f"C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2024\\day{PROBLEM}"
IN_PATTERN = "test.txt" if TEST == 1 else "input.txt"
IN_FILE = os.path.join(IN_DIR, IN_PATTERN)
NUMS = "0123456789"

def checksum(line):
  files = [int(i) for i in line]
  for_id = 0 # forward in files, file id
  index = 0 # actual index
  back_id = len(files) - 1 # backward in files, file id
  rem_in_j = files[back_id]
  total = 0
  while for_id < back_id:
    if for_id % 2 == 0:
      total += checksum_file(for_id/2, index, files[for_id])
      # print(index, i/2, files[i], j, total)
      index += files[for_id]
      for_id += 1
    else:
      empty_size = files[for_id]
      #print(index, for_id, empty_size, back_id/2, rem_in_j)
      while empty_size >= 0:
        if empty_size >= rem_in_j:
          total += checksum_file(back_id/2, index, rem_in_j)

          back_id -= 2
          empty_size -= rem_in_j
          index += rem_in_j
          rem_in_j = 0

          rem_in_j = files[back_id]
        else:
          total += checksum_file(back_id/2, index, empty_size)

          for_id += 1
          index += empty_size
          rem_in_j -= empty_size
          empty_size = 0
          break
  # print("rem", rem_in_j, for_id, back_id, index)
  if for_id == back_id and rem_in_j > 0:
    total += checksum_file(for_id/2, index, rem_in_j)

  return total

def checksum2(line):
  files = [int(i) for i in line]
  file_list = {} # file id to (position, len)
  #full = {} # position to (file id, len)
  empty = {} # position to len

  index = 0
  for i, f_len in enumerate(files):
    #print(i, f_len)
    if i % 2 == 0:
      file_list[int(i/2)] = (index, f_len)
      #full[index] = (int(i/2), f_len)
    else:
      if f_len > 0:
        empty[index] = f_len
    index += f_len

  # print(file_list)
  # print(empty)
  back_id = len(files) - 1
  while back_id > 0:
    int_back_id = int(back_id/2)
    file_pos, f_len = file_list[int_back_id]
    # print("-------")
    # print(file_list)
    # print(empty)
    for empty_pos in sorted(empty):
      empty_len = empty[empty_pos]
      # print(f"  {empty_pos} {empty_len} {file_pos} {f_len}")
      if file_pos < empty_pos:
        break
      if empty_len >= f_len:
        # move the file
        #del full[file_pos]
        file_pos = empty_pos
        file_list[int_back_id] = (file_pos, f_len)
        #full[file_pos] = (int_back_id, f_len)

        # update the empty
        empty.pop(empty_pos)
        if empty_len > f_len:
          empty[empty_pos + f_len] = empty_len - f_len
        break

    back_id -= 2

  total = 0
  for f_id, f_prop in file_list.items():
    total += checksum_file(f_id, f_prop[0], f_prop[1])
  return total

def checksum_file(file_id, start, length):
  # print(file_id, start, length, file_id * (start * length + length * (length - 1) / 2))
  return file_id * (start * length + length * (length - 1) / 2)




def main():
  with open(IN_FILE, 'r', encoding='utf-8') as f:
    for line in f:
      line = line.rstrip()
      print("-------")
      print("total: ", checksum(line))
      print("total2: ", checksum2(line))


if __name__ == "__main__":
  main()
