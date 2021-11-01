class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """        
        beg, end = 0, len(nums) - 1
        while beg <= end:
            middle = beg + ((end - beg) / 2) # this equation is to address overflow
            
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                beg = middle + 1
            elif nums[middle] > target:
                end = middle - 1
        
        # if loop terminates, target is not in the array
        return -1