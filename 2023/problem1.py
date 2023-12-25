import os

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_file = os.path.join(in_dir, "input1.txt")

nums = "123456789"
text_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
part = 2

def main():
  with open(in_file, 'r') as f:
    total = 0
    for line in f:
      line = line.rstrip()
      if not len(line):
        break

      first_i = -1
      last_i = -1
      for i in range(len(line)):
        if nums.find(line[i]) >= 0:
          last_i = i
          if first_i == -1:
            first_i = i

      first_val = 0
      if first_i >= 0:
        first_val = int(line[first_i])
      last_val = 0
      if last_i >= 0:        
        last_val = int(line[last_i])

      if part == 2:
        #print(line)
        #print(first_i, last_i, first_val, last_val)
        for i, text_num in enumerate(text_nums):
          index = line.find(text_num)
          index_b = line.rfind(text_num)
          if index < 0:
            continue
          if first_i < 0 or index < first_i:
            first_i = index
            first_val = i + 1
            #print("first", text_num, first_i, last_i, first_val, last_val)
          if last_i < 0 or index_b > last_i:
            last_i = index_b
            last_val = i + 1
              #print("last", text_num, first_i, last_i, first_val, last_val)

      val = 10 * first_val + last_val
      total += val
      print(line, val, total)
      #print('--------------')
    print("sum:", total)

num_to_val = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def main2():
  with open(in_file, 'r') as f:
    total = 0
    for line in f:
      line = line.rstrip()
      if not len(line):
        break

      first = -1
      last = -1
      for i in range(len(line)):
        for n, v in num_to_val.items():
          end = i + len(n)
          if end > len(line):
            continue
          if line[i:end] == n:
            last = v
            if first < 0:
              first = v
      total += 10 * first + last
      print(line, first, last)
    print("sum:", total)


if __name__=="__main__":
  main2()
