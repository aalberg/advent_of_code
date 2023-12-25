import os
import functools 
from collections import defaultdict

in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_file = os.path.join(in_dir, "input7.txt")

part = 2

nums = ""
if part == 2:
  nums = "J23456789TQKA"
else:
  nums = "23456789TJQKA"

def card_val(card):
  return nums.find(card)

def cmp_hand(hand1, hand2):
  if hand1.type != hand2.type:
    return hand1.type - hand2.type
  for i in range(5):
    v1, v2 = card_val(hand1.cards[i]), card_val(hand2.cards[i])
    if v2 != v1:
      return v1 - v2
  return 0

class Hand:
  def __init__(self, cards, bid):
    self.cards = [c for c in cards]
    self.bid = bid
    self.type = self.compute_type()

  def compute_type(self):
    card_map = defaultdict(int)
    for c in self.cards:
      card_map[c] += 1
    
    if part == 2:
      # Special case of JJJJJ
      if card_map["J"] == 5:
        return 10
      jokers = card_map["J"]
      if "J" in card_map:
        del card_map["J"]
      counts = sorted(list(card_map.values()), key=lambda x: -x)
      # Treat all the jokers like the thing we have the most of
      counts[0] += jokers
    else:
      counts = sorted(list(card_map.values()), key=lambda x: -x)

    # 10 = 5ok
    # 8 = 4ok
    # 7 = fh
    # 6 = 3ok
    # 5 = 2p
    # 4 = p
    # 2 = hk
    f = counts[0] * 2
    if f != 4 and f != 6:
      return f
    return f + (1 if counts[1] == 2 else 0)

  def __repr__(self):
    return str(self.cards) + " " + str(self.type)

hands = []

def main():
  with open(in_file, 'r') as f:
    for line in f:
      line = line.rstrip().split()
      hands.append(Hand(line[0], int(line[1])))
  
  total = 0
  for i, h in enumerate(sorted(hands, key=functools.cmp_to_key(cmp_hand))):
    #print(h)
    v = (i + 1) * h.bid
    total += v
  print("total", total)

if __name__=="__main__":
  main()
