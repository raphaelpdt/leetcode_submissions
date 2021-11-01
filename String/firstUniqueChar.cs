public class Solution {
    public int FirstUniqChar(string s) {
       if (s.Length == 1) return 0;
        
        Dictionary<char, List<int>> charDict = new Dictionary<char, List<int>>();
        for (int i = 0; i < s.Length; i++)
        {
            char curr = s[i];
            if (!charDict.ContainsKey(s[i]))
            {
                charDict.Add(s[i], new List<int>{i});       
            }
            else
            {
                charDict[s[i]].Add(i);
            }
        }
        
        foreach (var entry in charDict)
        {
            if (entry.Value.Count == 1)
            {
                return entry.Value[0];
            }
        }
        
        return -1;
    }
}