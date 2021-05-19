public class Solution {
    public bool IsAnagram(string s, string t) {
        // BASE CASE: return immediately if strings are not equal length
        if (s.Length != t.Length) 
            return false;
        // BASE CASE: any of the strings are empty, they cannot be anagrams
        if (s.Length == 0 || t.Length == 0)
            return false;
        
        // we can make use of a dict, where the keys are the letters in the string
        Dictionary<char, int> res = new Dictionary<char, int>();
        // build the dict with s, and upon finishing scanning t, all entries should count 0
        foreach (var c in s)
        {
            if (res.ContainsKey(c)) 
                res[c]++;
            else
                res.Add(c, 1);
        }
        
        foreach (var c in t)
        {
            // if at any point, we run into a character that does not exist in s or
            // the count goes below 0, return immediately
            if(!res.ContainsKey(c))
                return false;
            else 
            {
                if (res[c] <= 0) 
                    return false;
                else
                    res[c]--;
            } 
        }
        
        // the strings will be anagrams if we successfully iterate through both s and t,
        return true;
    }
}

// Test Cases:
// s = "anagram", t = "nagaram"
// s = "rat", t = "car"
// s = "", t = "yeehaw"
// s = "y" t = "y"
// s = "aacc", t = "ccac"