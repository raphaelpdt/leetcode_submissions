public class Solution {
    public bool WordBreak(string s, IList<string> wordDict) {
        bool[] dp = new bool[s.Length + 1];
        dp[0] = true;
        
        for (int i = 0; i < s.Length; i++)
        {
            if (dp[i])
            {
                foreach (var word in wordDict)
                {
                    if ((word.Length + i -1) < s.Length && String.Equals(s.Substring(i, word.Length), word))
                    {
                        dp[word.Length + i] = true;
                    }
                }
            }
        }
        
        return dp[s.Length];
    }
}