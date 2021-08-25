public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        // array representing cumulative product of all items to the left of curr item
        var left = new int[nums.Length]; 
        // array representing cumulative product of all items to the right of curr item
        var right = new int[nums.Length];
        var res = new int[nums.Length];
        
        for (int i = 0; i < nums.Length; ++i) {
            if (i==0) 
            { 
                left[i] = 1; 
            }
            else 
            {
                left[i] = left[i-1] * nums[i-1]; // product of items to the left of but not incl. nums[i]
            }
        }
        
        for (int i = nums.Length-1; i >= 0; --i) {
            if (i == nums.Length-1) 
            { 
                right[i] = 1; 
            }
            else 
            {
                right[i] = right[i+1] * nums[i+1];
            }
        }
        
        for (int i = 0; i < nums.Length; ++i) {
            res[i] = left[i] * right[i];
        }
        
        return res;
    }
}