#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'validateImageSize' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts following parameters:
#  1. 2D_STRING_ARRAY imageUrls
#  2. STRING maxSize
#

def validateImageSize(imageUrls, maxSize):
    # Write your code here
    # PSEUDOCODE:
    # Convert max size to an int representation
        # separate the number and the unit from the string representation
        # convert number to int
        # transform all unit chars to lower
            # multiply to int representation based on what's parsed from the unit
        
    #     Init result array
    #     Foreach image in imageUrls 
    #         compare if the image size is <= maxSize
        
    #     Return result array
    maxBytes = 0
    if maxSize == "none":
        maxBytes = 10**6
    else:
        maxSizeSplit = [] # array that will contain the number, and unit
        unit = ""
        for i in range(len(maxSize)):
            if maxSize[i].isalpha():
                maxBytes = int(maxSize[:i])
                unit = maxSize[i:].lower()
                break
        
        if unit == "kb":
            maxBytes *= 10**3
        elif unit == "mb":
            maxBytes *= 10**6
        else:
            maxBytes *= 10**9
    
    results = []
    for image in imageUrls:
        res = []
        res.append(image[0])
        if int(image[1]) <= maxBytes:
            res.append("TRUE")
        else:
            res.append("FALSE")
            
        results.append(res)
    
    return results
    
    

if __name__ == '__main__':