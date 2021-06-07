public class Solution
{
    public int FindMin(int[] nums)
    {
        // BASE CASE: Min. num would be the ONLY num in array
        if (nums.Length == 1) return nums[0];

        // init beg and ending pointers
        int beg = 0;
        int end = nums.Length - 1;
        // EDGE CASE: Array is not rotated
        if (nums[beg] < nums[end])
            return nums[beg];

        while (beg <= end)
        {
            int mid = (beg + end) / 2;
            int curr = nums[mid];

            // Check if we hit the 'Inflection Point'
            // we can return immediately if so
            if (curr > nums[mid + 1])
                return nums[mid + 1];
            else if (curr < nums[mid - 1])
                return curr;

            if (curr > nums[0])
                beg = mid + 1;
            else
                end = mid - 1;
        }

        return -1;
    }
}