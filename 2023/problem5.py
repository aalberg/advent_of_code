import os

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_file = os.path.join(in_dir, "input5.txt")
import time

maps = []

def nextline(f):
  line = f.readline()
  if not line:
    return ""
  line = line.rstrip()
  return line

class range_map():
  def __init__(self):
    self.ranges = []

  def insert(self, dest, source, length):
    self.ranges.append((source, source + length - 1, dest))

  # Maps a source number to a dest number using the range mappings.
  def lookup(self, source):
    for r in self.ranges:
      if source >= r[0] and source <= r[1]:
        return r[2] + source - r[0]
    return source

  # Returns a range containing source. There are 3 general cases
  # 1. If a range containing source exists, return it
  # 2. If no range containing source exists, and there is a range that starts
  #   after source, return a made up range from source to the start of tha
  #   range
  # 3. If no range containing source exists, and there is no range after source,
  #   return a made up range starting at source with length length
  def lookup_range(self, source, length):
    min_start = 10**20
    for r in self.ranges:
      if source >= r[0] and source <= r[1]:
        return r  # Case 1
      elif r[0] > source:
        min_start = min(min_start, r[0])
    if min_start != 10**20:
      return (source, min_start - 1, source)  # Case 2
    return (source, source + length - 1, source)  # Case 3

  # Transforms a starting range (start, length) to a set of new ranges
  # (start, length) using the stored range mappings. If the input spans multiple
  # ranges, break the input into multiple new ranges, each mapped appropriately
  # depending on how each element in the range would map
  def transform_range(self, r):
    cur = r[0]
    length = r[1]

    new_ranges = []
    while True:
      cur_r = self.lookup_range(cur, length)
      new_start = cur_r[2] + cur - cur_r[0]
      overlap_len = cur_r[1] - cur + 1
      
      # The range we found fully contains the remaining range to map
      if overlap_len >= length:
        new_ranges.append((new_start, length))
        return new_ranges
      # The range we found doesn't fully contain the remaining range to map
      # Break the range into 2 parts: the part that fits (and save it), then
      # adjust our start and remaining length and repeat.
      new_ranges.append((new_start, overlap_len))
      cur += overlap_len
      length -= overlap_len
    # Should be impossible
    exit(1)

  def __str__(self):
    return str(self.ranges)

  def __repr__(self):
    return str(self)

def main():
  with open(in_file, 'r') as f:
    seeds = [int(i) for i in nextline(f)[7:].split()]
    nextline(f)

    while True:
      line = nextline(f)
      if len(line) == 0:
        break
      new_map = range_map()
      while len(line := nextline(f)) > 0:
        dest, source, length = [int(i) for i in line.split()]
        new_map.insert(dest, source, length)
      maps.append(new_map)

    # Part 1
    #start_time = time.time()
    start = seeds
    end = []
    for seed_map in maps:
      end = [seed_map.lookup(s) for s in start]
      start = end
    print(min(end))
    #print("--- part 1: %s seconds ---" % (time.time() - start_time))

    # Part 2
    #start_time = time.time()
    start_r = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
    end_r = []
    for seed_map in maps:
      end_r = []
      for s in start_r:
        end_r.extend(seed_map.transform_range(s))
      start_r = end_r
    print(min([e[0] for e in end_r]))
    #print("--- part 2: %s seconds ---" % (time.time() - start_time))

if __name__=="__main__":
  start_time2 = time.time()
  main()
  print("--- overall: %s seconds ---" % (time.time() - start_time2))
