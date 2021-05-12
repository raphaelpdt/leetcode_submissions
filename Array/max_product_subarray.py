class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # EDGE CASES: empty list or list has only one entry
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        
        # set up variables to store the first entry of the list
        minSoFar = nums[0]
        maxSoFar = nums[0]
        res = nums[0]
        # iterate through the list from the second entry onwards
        for i in range(1, len(nums)):
            currMax = max(nums[i], max(maxSoFar * nums[i], minSoFar * nums[i]))
            currMin = min(nums[i], min(minSoFar * nums[i], maxSoFar * nums[i]))
            
            # store results for the next iteration
            maxSoFar = currMax
            minSoFar = currMin
            
            res = max(res, maxSoFar) # check if this iteration has a larger max than the prev
            
        return res


# First attempt (was almost there)
# The problem was: it couldn't properly handle edge cases where the array consisted of only negative numbers
# class Solution(object):
#     def maxProduct(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         curr_max = 1 # var to hold maximum product found in the subarray
#         curr_min = 1 # var to hold minimum product found in subarray
#         max_so_far = 0 # var to hold max product seen so far
#         flag = 0 # flags if a positive num has been encountered
        
#         for num in nums:
#             if num == 0:
#                 curr_max = curr_min = 1 # reset all values if current entry is 0
#             # if curr num is positive
#             elif num > 0:
#                 curr_max *= num
#                 curr_min = min(curr_min * num, 1)
#                 flag = 1 # flag the fact that a positive num has been encountered
#             # the curr num is negative
#             else:
#                 temp = curr_max # store curr_max before modifying it
#                 curr_max = max(curr_min * num, 1) 
#                 curr_min = temp * num
            
#             # update max_so_far if current running subarray is greater than recorded
#             # max so far
#             if curr_max > max_so_far:
#                 max_so_far = curr_max
                
        
#         if flag == 0 and max_so_far == 0: return 0 # no positive num encountered, therefore max product is 0
#         return max_so_far

