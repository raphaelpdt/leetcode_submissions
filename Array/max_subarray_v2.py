class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float("-inf") # set result as smallest possible number
        sum_so_far = 0 # var to represent the sum-so-far
        
        # iterate through the list
        for num in nums:
            sum_so_far += num
            # if the current sum is greater than the set res
            if res < sum_so_far:
                res = sum_so_far
            # if adding to the curr sum makes it 0
            if sum_so_far < 0:
                sum_so_far = 0 # reset msf to 0 if newest addition set it to 0
                
        return res

# Test cases
# [-2,1,-3,4,-1,2,1,-5,4]
# [1]
# [5,4,-1,7,8]
# [-2,-1,3,2,-3]