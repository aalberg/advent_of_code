import os
from collections import deque

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_file = os.path.join(in_dir, "input4.txt")

nums = "0123456789"

def main():
  with open(in_file, 'r') as f:
    total = 0
    total_cards = 0
    future_copies = deque()
    for line in f:
      line = line.rstrip().split(": ")[1]
      winning, mine = line.split(" | ")
      winning = [int(i) for i in filter(None, winning.split(" "))]
      winning_map = {i : True for i in winning}
      mine = [int(i) for i in filter(None, mine.split(" "))]

      count = 0
      for m in mine:
        if m in winning_map:
          count += 1


      cur_cards = 1
      if len(future_copies) > 0:
        cur_cards += future_copies.popleft()
      total_cards += cur_cards
      #print("cur_cards", cur_cards)

      for i in range(count):
        if i + 1 > len(future_copies):
          future_copies.append(cur_cards)
        else:
          future_copies[i] += cur_cards
      #print("future_copies", future_copies)
      if count > 0:
        total += 2 ** (count - 1)
      #print("------")
    print("sum:", total)
    print("total_cards:", total_cards)



if __name__=="__main__":
  main()
