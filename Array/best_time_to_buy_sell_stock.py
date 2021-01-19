class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        
        # set buy to max num, and profit (currMax) to 0
        buy, profit = float('inf'), 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            # recalc price as long as selling a stock is profitable,
            # keep track of largest profit
            else:
                profit = max(profit, prices[i] - buy)
        
        return profit