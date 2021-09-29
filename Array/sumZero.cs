public class Solution {
    public int[] SumZero(int n) {
        // BASE CASE: only one number needed for the array
        if (n == 1) {
            return new int[] {0};
        }
        
        int[] result = new int[n];
        // set up ptrs to point at each end of the array
        int left = 0;
        int right = n-1;
        int entry = 1;
        while (left < right)
        {
            // insert symmetric (-x, +x) vals to the array
            result[left] = entry * -1;
            result[right] = entry;
            
            // move ptrs and increment entry to insert
            left++; right--;
            entry++;
        }
        
        if (left == right) result[left] = 0; // insert 0 if n is odd
        
        return result;
    }
}

// RUNTIME: O(log n), simultaneously add two values per step, terminate at midpt
// SPACE COMPLEXITY: O(n), built up array of size n