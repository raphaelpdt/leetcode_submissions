public class Solution {
    public int ClimbStairs(int n) {
        // BASE CASE: either 1 or 2 steps
        if (n == 1) return 1;
        if (n == 2) return 2;
        
        // pre-populate results with base cases, future results will use these numbers
        int[] stepCounter = new int[n];
        stepCounter[0] = 1;
        stepCounter[1] = 2;
        for (int i = 2; i < n; i++)
        {
            stepCounter[i] = stepCounter[i-2] + stepCounter[i-1];
        }
        
        return stepCounter[n-1];
    }
}