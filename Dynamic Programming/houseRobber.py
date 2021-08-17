class HouseRobber(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        
        # init dp array and pre-populate with the first two values of the num array
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            # add greatest number between the previous entry or
            # robbing from 2 houses down and adding curr entry
            # each entry in dp should be max amount available because of this design
            dp.append(max(dp[i-2] + nums[i], dp[i-1]))
        
        return dp[len(nums) - 1]

class HouseRobberII(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        
        # run two calls of House Robber, one with everything but the last entry,
        # then another with everything but the first entry
        firstRun = self.robHouse(nums[:len(nums)-1])
        secondRun = self.robHouse(nums[1:])
        
        return max(firstRun, secondRun)
    
    def robHouse(self, nums):
        # init dp array and pre-populate with the first two values of the num array
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            # add greatest number between the previous entry or
            # robbing from 2 houses down and adding curr entry
            # each entry in dp should be max amount available because of this design
            dp.append(max(dp[i-2] + nums[i], dp[i-1]))
        
        return dp[len(nums) - 1]