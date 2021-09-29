#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'segment' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER_ARRAY space
#

def segment(x, space):
    # Write your code here
    # Init a result array to store min values per segment
    # Set up a for loop for space
        # Break each set of computers into segments of size x
        # Grab the minimum for each segment
    # Once done iterating through the computers, return max of result array
    # BASE CASE: segment size is 1
    if x == 1: return max(space)

    n = len(space) 
    result = []
    for i in range(n):
        # add the min. value in the segment to the results array
        currSegment = space[i:i+x]
        
        # exit immediately if curr segment is less than x
        if len(currSegment) < x:
            break
        
        result.append(min(currSegment))
    
    return max(result)
        
    
if __name__ == '__main__':