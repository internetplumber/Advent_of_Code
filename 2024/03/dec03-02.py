#!/usr/bin/python3

import re

mul_regex = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
val_regex = r'\d{1,3}'

sum = 0
active = 1
with open("dec03-input.txt", 'r') as dataFile:
	for line in dataFile:
		tokens = re.findall(mul_regex, line)
		for token in tokens:
			if token == "don't()":
				active = 0
				next
			elif token == "do()":
				active = 1
			elif active == 1:
				vals = re.findall(val_regex, token)
				sum += int(vals[0]) * int(vals[1])

print(sum)
