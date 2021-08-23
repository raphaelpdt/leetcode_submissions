class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        numsLen = len(nums)
        dp = [1 for _ in range(numsLen)]
        
        # Outer Loop: fast pointer
        for j in range(1, numsLen):
            # Inner Loop: slow pointer
            for i in range(0, j):
                # If number ahead is greater AND current entry is less than prev entry
                # with an increment
                if nums[j] > nums[i] and dp[j] < dp[i] + 1:
                    dp[j] = dp[i] + 1
        
        return max(dp)

    # NOTE: each entry in dp array signifies longest increasing subsequence at that point
    # NOTE: at each step in the algorithm, we compare the slow pointer to every previous entry