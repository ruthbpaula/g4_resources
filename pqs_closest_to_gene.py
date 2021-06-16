# -*- coding: utf-8 -*-
"""
Created on Wed Jun 09 14:00:01 2021

@author: Ruth De Paula and Luciano Branco
"""

import pandas as pd
import numpy as np
import math
import numpy.matlib
import sys

# # arg1 = sys.argv[1]
arg1 = '500_first_splice_g4_counts_3_100.txt' # input file with counts

file_toPlot = pd.read_csv(arg1, delimiter = '\t', names = ['strand', 'gene', 'ss_chr', 'ss_coord', 'pqs_chr', 'pqs_coord', 'distance'])

#sort according to pqs_chr and pqs_coord
sorted_df_old_index = file_toPlot.sort_values(["pqs_chr", "pqs_coord"])
sorted_df = sorted_df_old_index.reset_index(drop=True)

#if sorting numpy:
#ind = np.lexsort((file_toPlot["pqs_chr"], file_toPlot["pqs_coord"]))
#sorted_df = file_toPlot[ind]

# start empty dataframe
output_dataframe = pd.DataFrame(columns = sorted_df.columns.tolist())

line_idx = 0
#for line_idx in range(0, len(sorted_df.index) -1 ):
while line_idx < len(sorted_df.index)-1:
    if (sorted_df.pqs_chr[line_idx] == sorted_df.pqs_chr[line_idx+1]):
        # Same pqs_chr here.
        
        if (sorted_df.pqs_coord[line_idx] == sorted_df.pqs_coord[line_idx+1]):
            # Same pqs_coord here. Find the closest to splice site.
            
            if (abs(sorted_df.ss_coord[line_idx] - sorted_df.pqs_coord[line_idx]) 
                < 
                abs(sorted_df.ss_coord[line_idx+1] - sorted_df.pqs_coord[line_idx+1])
                ):
                # Save line_idx
                line_contents = sorted_df[line_idx : line_idx+1]
                
            else:
                # Save line_idx + 1
                line_contents = sorted_df[line_idx+1 : line_idx+2]
            
        else: # pqs_coord are different.
            # Save both lines
            line_contents = sorted_df[line_idx : line_idx+2]
            
        output_dataframe = output_dataframe.append(line_contents)
        # Jump one line because we already looked at 2 lines !
        line_idx = line_idx+2

if len(sorted_df.index) % 2 != 0:
    line_contents = sorted_df[line_idx : line_idx+1]

    output_dataframe = output_dataframe.append(line_contents)

# Prep output file:
output_filename = '500_first_splice_g4_counts_3_100_output.txt'
output_dataframe.to_csv(output_filename, sep='\t', index=False)







