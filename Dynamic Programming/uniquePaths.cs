public class Solution
{
    public int UniquePaths(int m, int n)
    {
        // BASE CASE
        if (m == 1 && n == 1) return 1;

        // Build a grid that will solve number of unique paths
        // per tile
        int[,] dp = new int[m, n];

        // pre-populate top row and first column
        for (int i = 0; i < n; i++)
        {
            dp[0, i] = 1;
        }

        for (int i = 0; i < m; i++)
        {
            dp[i, 0] = 1;
        }

        for (int i = 1; i < m; i++)
        {
            for (int j = 1; j < n; j++)
            {
                dp[i, j] = dp[i - 1, j] + dp[i, j - 1];
            }
        }

        return dp[m - 1, n - 1]; // return bottom right row of dp grid
    }
}