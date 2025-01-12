#!/usr/bin/python3
# https://adventofcode.com/2024/day/2#part2

# Looks like I've got the wrong end of the stick with this at the moment, because we with the dampener we need to look
# at the line as a whole, not each transition. So the value of n must be a difference of between 2 and 6 of n-2.

# New plan.  Iterate twice over the line.  First time, decide if it is an incrementing or a decrementing series.  Second
# time, check each number obeys the rules.  If the previous number didn't obey the rules, check according to two numbers
# back.

# How do we figure out if a line is incrementing?  Ignore values that are equal, or when difference > 3. Otherwise sum
# up the number of increments and decrements. Greatest number will be what the line is doing (other should only be 1)

def isSafe(lineList, isRecursive):
	numInc = 0
	numDec = 0
	numErr = 0
	for index in range(1, len(lineList)):
		prev = int(lineList[index-1])
		cur = int(lineList[index])
		if (prev == cur) or (abs(prev-cur) > 3):
			numErr += 1
		elif prev < cur:
			numInc += 1
		elif prev > cur:
			numDec += 1
	if ((numInc == 0) or (numDec == 0)) and (numErr == 0):
		return 1
	else:
		if isRecursive == 1:
			return 0
		else:
			# Brute force approach. Don't try and find the aberrant value and knock it out, just try knocking each
			# value out in turn. If any of the sublists are valid, then we're good.
			for index in range(len(lineList)):
				shortList = lineList.copy()
				del shortList[index]
				if isSafe(shortList, 1):
					return 1
	return 0


safeCount = 0
with open("data02.txt", 'r') as dataFile:
	for line in dataFile:
		line.rstrip()
		lineList = line.split()

		safeVal = isSafe(lineList, 0)

		if safeVal == 1:
			safeCount += 1

print('Safe lines = ', safeCount)

# vim: ts=4: tw=120
