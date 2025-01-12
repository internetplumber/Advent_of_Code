#!/usr/bin/python3

col1 = []
col2 = []
totDist = 0

# Open the input file
dataFile = open("datafile.txt", "r")

# Iterate over the input file, split the input lines and append into col1 and col2 lists.
for inputLine in dataFile:
	inputLine.rstrip()
	(a, b) = inputLine.split()
	col1.append(int(a))
	col2.append(int(b))

# Close the input file
dataFile.close()

col1.sort()
#print("Sorted col1: ", col1)

# Iterate over col1, find lowest value in col2, calculate difference, delete elements from both lists
for i in col1:
	#print("Col 1: ", i)
	col2min = min(col2)
	#print("Col 2: ", col2min)
	distance = abs(col2min - i)
	#print("Distance: ", distance)
	totDist += distance
	col2.remove(col2min)

print("Total Distance: ", totDist)
