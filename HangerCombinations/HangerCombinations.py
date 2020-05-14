from itertools import combinations
from pprint import pprint

while True:
    try:
        print('Place a txt file in the same folder as this file.\nList all possible options like so: Option 1, Option 2, Option 3, ... \nCase insensitive.')
        fileName = input('Enter the name of the txt file: ')
        openFile = open(fileName + ".txt", "r").read()
        break
    except:
        print("File not found!\n\n")

values = openFile.split(",")
sVals = []
for val in values:
    val = val.strip()
    sVals.append(val)
valLength = len(sVals)
i = 1
while i <= valLength:
    comb = combinations(sVals, i)
    for c in list(comb):
        with open(fileName + ".txt", "a") as f:
            f.write("\n" + str(c) + "\n")
    i += 1

print("\nDone!\n")