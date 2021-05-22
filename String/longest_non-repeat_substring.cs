public class Solution
{
    public int LengthOfLongestSubstring(string s)
    {
        // BASE CASE: empty string
        if (String.IsNullOrEmpty(s))
        {
            return 0;
        }
        // BASE CASE: string of length 1 will trivially have a substring of 1
        if (s.Length == 1)
        {
            return 1;
        }


        int res = 0;
        int i = 0; // count of chars removed
        int j = 0; // count of chars traversed in string
        int len = s.Length;
        // hashset to store  currently processed letters
        HashSet<char> substringChars = new HashSet<char>();
        while (i < len && j < len)
        {
            // add new character to set, then increment j
            if (!substringChars.Contains(s[j]))
            {
                substringChars.Add(s[j]);
                j++;
                // j-i will represent chars counted - chars removed, therefore
                // calculating the offset
                res = Math.Max(res, j - i);
            }
            else
            {
                // remove first occurrence of the char
                substringChars.Remove(s[i]);
                // increment counter of removed chars, in next iteration
                // curr char (s[j]) will be added back in order to count next substr
                i++;
            }
        }

        return res;
    }
}