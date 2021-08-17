class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # build an array composed of max val, since we will build up array while comparing minimum values
        dp = [float('inf')]*(amount+1) 
        dp[0] = 0 # you can make change for amount = 0, 0 ways
        
        # Outer Loop: our available options
        for coin in coins:
            # Inner loop: Numbers from coin val - target amount
            for j in range(coin, amount+1):
                # what is the minimal amount of coins we can use to get to "i" 
                # with our given options
                dp[j] = min(dp[j], 1+dp[j-coin]) 
        
        return dp[amount] if dp[amount] != float('inf') else -1