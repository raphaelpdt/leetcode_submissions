class Solution(object):
    res = 0
    
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        self.backtrack(0, arr, "")
        return self.res
    
    def backtrack(self, i, arr, curr):
        """
        :type uniqueChars: Set[char]
        :type i: int
        :type arr: List[str]
        :rtype: void
        """
        if len(curr) != len(set(curr)):
            return
        
        self.res = max(self.res, len(curr))
        for i in range(i, len(arr)):
            self.backtrack(i+1, arr, curr + arr[i])