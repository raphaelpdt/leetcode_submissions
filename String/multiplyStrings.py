class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ## use the same logic as add strings
            # create int representations of each string
                # build up by multiplying the factor to the int, start from the lowest digit
            # multiply the two ints and return the result as a string
        int1 = int2 = 0
        
        factor = 1
        for digit in num1[::-1]:
            int1 += int(digit) * factor
            factor *= 10
        
        factor = 1
        for digit in num2[::-1]:
            int2 += int(digit) * factor
            factor *= 10
        
        return str(int1 * int2)