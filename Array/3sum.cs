public class Solution {
    public IList<IList<int>> ThreeSum(int[] nums) {
        var result = new List<IList<int>> ();
        
        if (nums == null) return result;
        
        Array.Sort(nums);
        for (int i = 0; i < nums.Length - 2; i++)
        {
            // return immediately as no combination will satisfy 3Sum if left-most num is positive
            if (nums[i] > 0) return result; 
            if (i > 0 && nums[i] == nums[i-1]) continue; // move index until it's no longer next to a dup
            
            int left = i + 1;
            int right = nums.Length - 1;
            while (left < right)
            {
                int sum = nums[i] + nums[left] + nums[right];
                // we need to add a smaller number, move right ptr
                if (sum > 0)
                {
                    right--;
                }
                // we need to add a greater number, move left ptr
                else if (sum < 0)
                {
                    left++;
                }
                else
                {
                    result.Add(new List<int>{nums[i], nums[left], nums[right]});
                    
                    // move ptrs until they are no longer next to duplicates
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    left++; right--;
                }
            }
        }
        
        return result;
    }
}