#!/usr/bin/python3

import re

mul_regex = r'mul\(\d{1,3},\d{1,3}\)'
val_regex = r'\d{1,3}'

sum = 0
with open("dec03-input.txt", 'r') as dataFile:
	for line in dataFile:
		mults = re.findall(mul_regex, line)
		for instruction in mults:
			vals = re.findall(val_regex, instruction)
			sum += int(vals[0]) * int(vals[1])

print(sum)
