#!/bin/python
import random

text = None
path_to_dictionary_file = "/usr/share/cracklib/cracklib-small"

with open(path_to_dictionary_file) as f:
  text = f.read()
  f.close()

words = text.split("\n")
random_set = []

for i in range(1000):
  w = words.pop( random.randint(0, len(words) - 1) )
  random_set.append(w)

strings = ["\"" + s + "\"" for s in random_set if len(s) > 4]
print(len(strings))
words = "var randomWords = [" + str.join(", ", strings[:200]) + "]"
print(words)
