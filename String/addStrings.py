class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ## PSEUDOCODE ##
        # init var to represent factor to multiply by
        # init var for resulting sum
        # init vars representing the int representations of each number
        
        # iterate through each string in reverse to create an int representation
        # of num1 and num2
        
        # return number1 + number2
        
        int1 = int2 = 0
        factor = 1
        for digit in reversed(num1):
            int1 += int(digit) * factor
            factor *= 10
        
        factor = 1 # reset factor for next number conversion
        for digit in reversed(num2):
            int2 += int(digit) * factor
            factor *= 10
        
        return str(int1 + int2)