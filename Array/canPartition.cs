public class Solution {
    public bool CanPartitionKSubsets(int[] nums, int k) {
        if (nums.Length == 1 && k == 1) return true;
        
        int sum = nums.Sum();
        // determine target number
        if (sum % k != 0) return false;
        bool[] visited = new bool[nums.Length];
        Array.Sort(nums);
        
        return dfs(nums, 0, nums.Length - 1, visited, sum / k, k);
    }
    
    public bool dfs(int[] nums, int sum, int start_idx, bool[] visited, int target, int round) 
    {
        if (round == 0) return true;
        if (sum == target && dfs(nums, 0,  nums.Length-1, visited, target, round - 1)) return true;
        
        for (int i = start_idx; i >= 0; i--)
        {
            int curr_sum = sum + nums[i];
            if (!visited[i] && curr_sum <= target) {
                visited[i] = true;
                
                if (dfs(nums, curr_sum, i, visited, target, round))
                {
                    return true;
                }
                
                visited[i] = false;
            }
        }
        
        return false;
    }
}