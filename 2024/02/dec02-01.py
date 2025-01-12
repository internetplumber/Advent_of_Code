#!/usr/bin/python3

safeCount = 0
with open("data02.txt", 'r') as dataFile:
	for line in dataFile:
		print('New line')
		line.rstrip()
		lineList = line.split()
		lineLen = len(lineList)
		isInc = -1
		safe = 1
		for index in range(1, lineLen):
			prev = int(lineList[index-1])
			cur = int(lineList[index])
			print('Prev = ', prev, ', cur = ', cur)
			if prev == cur:
				safe = 0
				break
			elif abs(prev - cur) > 3:
				safe = 0
				break
			elif (isInc == -1) and (prev > cur):
				print('Line is decrementing')
				isInc = 0
				continue
			elif (isInc == -1) and (prev < cur):
				print('Line is incrementing')
				isInc = 1
				continue
			elif (isInc == 1) and (prev > cur):
				safe = 0
				break
			elif (isInc == 0) and (prev < cur):
				safe = 0
				break
			else:
				continue
		if safe == 1:
			print('Safe line: ', lineList)
			safeCount += 1

print('Safe lines = ', safeCount)

# vim: ts=4
