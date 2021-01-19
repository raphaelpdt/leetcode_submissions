class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, curr = float('-inf'), 0
        for i in range(len(nums)):
            curr = max(nums[i], nums[i] + curr)
            
            if res < curr:
                res = curr
        
        return res   