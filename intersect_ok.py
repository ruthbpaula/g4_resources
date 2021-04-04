# coding=utf-8
## intersect_ok.py - intersecting files
## Written by: Luciano Branco and Ruth De Paula - 2020

import os
import sys
import pandas as pd
import numpy as np

def positionsAreOverlapping(position1, position2):
        if position2[left] <= position1[left] <= position2[right] or position2[left] <= position1[right] <= position2[right]:
                return True
        else:
                return False


def linesMatch(line_file1, line_file2):
        positions_file1 = [file1.iloc[line_file1, start_idx], file1.iloc[line_file1, end_idx]]
        positions_file2 = [file2.iloc[line_file2, start_idx], file2.iloc[line_file2, end_idx]] 

        if file1.iloc[line_file1, chr_idx] == file2.iloc[line_file2, chr_idx]: # Match chromosome names
                if positionsAreOverlapping(positions_file1, positions_file2) or positionsAreOverlapping(positions_file2, positions_file1):
                        return True


def writeMatchToFile(line_file1, line_file2, output_file):
        # Match  pos:
        startMatch = max(file2.iloc[line_file2, start_idx], file1.iloc[line_file1, start_idx])
        endMatch = min(file2.iloc[line_file2, end_idx], file1.iloc[line_file1, end_idx])
        sizeMatch = (endMatch - startMatch) + 1
        # Prepare matchLine to write
        matchLine = str(file1.iloc[line_file1,0]) + "\t" + str(startMatch) + "\t" + str(endMatch) + "\t" + str(sizeMatch) + "\t" + str(file2.iloc[line_file2,3])
        # Write the matchLine
        output_file.write(matchLine)


arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]

file1 = pd.read_csv(arg1, delimiter = '\t', names = ['chr', 'start', 'end'])
file2 = pd.read_csv(arg2, delimiter = '\t', names = ['chr', 'start', 'end', 'gene'])

output_file= open(arg3,"w")

chr_idx = 0
start_idx = 1
end_idx = 2

left = 0
right = 1

firstMatchFound = False
for line_file1 in range(0, (file1.shape[0])):
        for line_file2 in range(0, (file2.shape[0])):
                if linesMatch(line_file1, line_file2):
                        writeMatchToFile(line_file1, line_file2, output_file)
                        firstMatchFound = True
                        break

        if firstMatchFound:
                break

for line_file1 in range(1, (file1.shape[0])):
        for line_file2 in range(0, (file2.shape[0])):
                if file2.iloc[line_file2, chr_idx] > file1.iloc[line_file1, chr_idx]: # I can stop the search
                        break
                if linesMatch(line_file1, line_file2):
                        output_file.write("\n")
                        writeMatchToFile(line_file1, line_file2, output_file)

del file1
del file2
output_file.close()
