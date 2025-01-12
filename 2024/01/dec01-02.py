#!/usr/bin/python3

col1 = []
col2 = []
totSim = 0

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

# Iterate over col1, find lowest value in col2, calculate difference, delete elements from both lists
for i in col1:
	similarity = i * col2.count(i)
	totSim += similarity

print("Total Similarity: ", totSim)
