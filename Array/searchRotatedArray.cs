public class Solution {
    public int Search(int[] nums, int target) {
        if (nums.Length == 0) return -1;
        
        // use a binary search style approach
        int beg = 0;
        int end = nums.Length - 1;
        while (beg <= end)
        {
            // add beg to end to account for offset while traversing list
            int mid = (beg + end) / 2; 
            
            // return immediately if target is hit
            if (nums[mid] == target)
                return mid;
            else if (nums[mid] >= nums[beg])
            {
                // check if target is between beg and mid
                if (nums[beg] <= target && target <= nums[mid])
                    end = mid;
                // target must be greater than mid, so set beg 
                // to after mid
                else
                    beg = mid+1;
            }
            else
            {
                // check if target is between mid and end
                if (nums[mid] <= target && target <= nums[end])
                    beg = mid+1;
                else
                    end = mid;
            }
        }
        
        return -1; // did not find a match in the array
    }
}