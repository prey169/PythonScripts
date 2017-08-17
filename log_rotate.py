#!/usr/bin/env python3
import os
import re

os.chdir("/Users/frossi/Python/test")

files = os.listdir(".")
regex = "^a(.?\d*)?$"
goodfiles = []
numbers = []

for i in files:
    if re.match(regex, i) != None:
        goodfiles.append(i)

for i in goodfiles:
    if i == 'a.':
        continue
    if "." in i:
        numbers.append(int(i.strip("a.")))

numbers=sorted(numbers, reverse=True)

for i in numbers:
    os.rename("a." + str(i), "a." + str(i+1))

if 'a' in files:
    os.rename("a", "a.1") 

