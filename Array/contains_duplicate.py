class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        res = set()
        
        for i in nums:
            if i in res: return True
            res.add(i)
        
        # no duplicate found in the list
        return False