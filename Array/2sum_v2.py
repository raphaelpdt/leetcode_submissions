class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # build a dict where the key is sum between certain numbers
        sum_dict = {}
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                curr_sum = nums[i] + nums[j]
                if curr_sum == target: return [i, j]
                
                if curr_sum in sum_dict:
                    continue
                
                sum_dict[curr_sum] = [i,j] # this assumes that all sums are unique
                
        
        # no such entry with target exists
        return [0,0]