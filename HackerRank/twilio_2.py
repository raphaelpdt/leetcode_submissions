#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'validatePhoneNumberFormat' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING address as parameter.
#

def validatePhoneNumberFormat(address):
    # Write your code here
    ## PSEUDOCODE: 
    # parse the address
        # is there a provider? then split string from ":"
            # to check if no provider is given by attempting split, if array is len of 1,
            # no provider should have been given
        # if no provider OR provider ids E.164, is it a valid E.164 number?
            # should check if each char is a digit, if not, exit immediately
        # else check if all characters are alphanumeric and of sufficient length
    
    splitAddress = address.split(":")
    provider = ""
    identifier = None
    if len(splitAddress) > 1:
        provider = splitAddress[0].lower()
        identifier = splitAddress[1]
    else:
        provider = "sms"
        identifier = splitAddress[0]
    
    print(provider)
    print(identifier)
    
    # check for valid e.164 address
    if provider == "sms" or provider == "whatsapp" or provider == "messenger":
        # remove "+" symbol from identifier and modify id var accordingly
        splitNumber = identifier.split("+")
        identifier = splitNumber[0]
        if len(splitNumber) > 1:
            identifier = splitNumber[1]
        
        if len(identifier) <= 15 and identifier.isnumeric():
            return provider.upper()
        else:
            return "INVALID_ADDRESS"
    # check for valid addresses that are not e.164
    elif len(splitAddress[1]) <= 248 or splitAddress[1].isalnum():
        # init a set of acceptable characters that are not alphanum
        acceptableCharacters = ['+', '-', '_', '@', '.']
        if identifier.isalnum():
            return provider.upper()
        #elif 
        
    return "INVALID_ADDRESS"

if __name__ == '__main__':