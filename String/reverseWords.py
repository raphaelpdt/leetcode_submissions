class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Preprocess: trim the string then split the string by the spaces between words
        s = s.strip()
        words = s.split()
        
        if len(words) == 1: return words[0]
        
        # join the entries of the split array in reverse order, join the entries with
        # a space
        words.reverse()
        return " ".join(words)