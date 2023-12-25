import bisect
from collections import defaultdict
from collections import deque
import functools
import math
import os
import time

PART = 1
TEST = 0
PROBLEM = 20
in_dir = "C:\\Users\\Alex\\Documents\\Projects\\advent_of_code\\2023\\"
in_pattern = "test%d_2.txt" if TEST == 1 else "input%d.txt"
in_file = os.path.join(in_dir, in_pattern % PROBLEM)
NUMS = "0123456789"

class Module:
  def __init__(self, name):
    self.name = name

  def add_input(self, name):
    pass

  def handle_pulse(self, source, high):
    pass

  def __str__(self):
    return self.__repr__()

class Broadcast(Module):
  def __init__(self, name, outputs):
    Module.__init__(self, name)
    self.outputs = outputs

  def handle_pulse(self, source, high):
    signals = []
    for o in self.outputs:
      signals.append((self.name, high, o))
    return signals

  def __repr__(self):
    return "B: " + self.name + ": " + " ".join(self.outputs)

class FlipFlop(Module):
  def __init__(self, name, outputs):
    Module.__init__(self, name)
    self.on = False
    self.outputs = outputs

  def handle_pulse(self, source, high):
    signals = []
    if not high:
      self.on = not self.on
      for o in self.outputs:
        signals.append((self.name, self.on, o))
    return signals

  def __repr__(self):
    #return "F: " + self.name + ": " + " ".join(self.outputs)
    return "F: " + self.name + " " + str(self.on)

class Conjunction(Module):
  def __init__(self, name, outputs):
    Module.__init__(self, name)
    self.outputs = outputs
    self.memory = {}

  def add_input(self, name):
    self.memory[name] = False

  def handle_pulse(self, source, high):
    self.memory[source] = high
    ok = True
    for _, v in self.memory.items():
      ok &= v
    signals = []
    for o in self.outputs:
      signals.append((self.name, not ok, o))
    return signals

  def __repr__(self):
    #return "C: " + self.name + ": " + " ".join(self.outputs)
    return "C: " + self.name + " " + str(self.memory)


modules = {}

def print_modules():
  print("-------")
  for m in modules.values():
    print(m)

LIMIT = 10**3
overall_i = 1
cycles = defaultdict(list)

def press_button():
  #print("=================")
  pulse_count = [0, 1]
  cur = modules["broadcaster"].handle_pulse("", False)
  i = 0
  while len(cur) > 0 and i < LIMIT:
    #print("-------")
    #print("cur", cur)
    next_state = []
    for s, p, d in cur:
      #print(s, p, d)
      if p:
        pulse_count[0] += 1
      else:
        pulse_count[1] += 1
      if d == "dh" and p:
        cycles[s].append(overall_i)# - cycles[s]
        #print(overall_i, s, p, d)
      if d == "rx" and not p:
        print("done")
        return None
      pulses = modules[d].handle_pulse(s, p)
      # if len(pulses) > 0:
      #print("  pulses from", s, pulses)
      next_state.extend(pulses)
    cur = next_state
    i += 1
  #print_modules()
  #print(modules["hd"])
  if i >= LIMIT:
    print("BADBAD")
    exit(1)
  #print(i, pulse_count)
  return pulse_count

def main():
  global overall_i
  with open(in_file, 'r') as f:
    for line in f:
      line = line.rstrip().split(" -> ")
      module_type = line[0][0]
      module_name = line[0][1:]
      modules_to = line[1].split(", ")
      #print(module_type, module_name, modules_to)

      if module_type == "%":
        modules[module_name] = FlipFlop(module_name, modules_to)
      elif module_type == "&":
        modules[module_name] = Conjunction(module_name, modules_to)
      else:
        modules["broadcaster"] = Broadcast("broadcaster", modules_to)

  missing = []
  for m in modules.values():
    for o in m.outputs:
      if o not in modules:
        missing.append(o)
  for m in missing:
    modules[m] = Conjunction(m, [])
  for m in modules.values():
    for o in m.outputs:
      modules[o].add_input(m.name)

  overall_count = [0, 0]
  for i in range(100000):
    pulses = press_button()
    if pulses == None:
      print("done", i)
      break
    for i in range(len(overall_count)):
      overall_count[i] += pulses[i]
    overall_i += 1
  print("overall_count", overall_count, overall_count[0] * overall_count[1])
  print("cycles", cycles)

if __name__=="__main__":
  main()
