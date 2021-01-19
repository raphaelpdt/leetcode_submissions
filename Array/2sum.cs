public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var targetIndices = new int[2];
        
        for (int i = 0; i < nums.Count(); i++) {
            for (int j = i + 1; j < nums.Count(); j++) {
                if (nums[i] + nums[j] == target) 
                {
                    targetIndices[0] = i;
                    targetIndices[1] = j;                                    
                }
            }    
        }
        
        return targetIndices;
        //throw new IllegalArgumentException("No TwoSum solution exists");
    }
}