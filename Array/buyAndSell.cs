public class Solution {
    public int MaxProfit(int[] prices) {
        int profit = 0;
        int buy = Int32.MaxValue;
        for (int i = 0; i < prices.Length; i++)
        {
            if (prices[i] < buy)
            {
                buy = prices[i];
            }
            else
            {
                profit = Math.Max(profit, prices[i] - buy);
            }
        }
        
        return profit;
    }
}