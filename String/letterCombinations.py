class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        
        keyPairings = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl", 
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }
        
        res = []
        queue = deque()
        queue.append("")
        
        numDigits = len(digits)
        while queue:
            currString = queue.popleft()
            stringLen = len(currString) # stringLen will represent how many digits are currently inputted
            
            # if a string is equal to the length of digits given, we have a complete combination
            if stringLen == numDigits:
                res.append(currString)
            else:
                # add a combination for each letter in the curr digit to the queue
                currDigit = digits[stringLen]
                for letter in keyPairings[currDigit]:
                    queue.append(currString + letter)
        
        return res