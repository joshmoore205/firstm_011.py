#!/usr/bin/env python3

# txt = "Mickey Mouse was a kind of mouse. Mickey Mouse was a kind of mouse. A mouse with a sense of humour."
import sys

#lines = sys.stdin.readlines()
#for line in lines:
#  line = line.strip()
#  yes = line.startswith("M", 0, 1)
#  if yes == True:
#    if "m" in line and:
#      new = line.replace("m", "M")
#      print(new)

lines = sys.stdin.readlines()
for line in lines:
  line = line.strip()
  newline = line.replace("m", "M", 1)
  print(newline)

