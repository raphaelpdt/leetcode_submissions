class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # BASE CASES: empty string cannot be a palindrome, a string with one character
        # is trivially a palindrome
        if len(s) == 0: return False
        if len(s) == 1: return True
        
        # as we will only consider alphanumeric characters, cast all characters
        # to lower case. Trim whitespace off the string, ignore any character
        # that is not alphanumeric.
        s = s.lower()
        s = s.strip()

        # use two pointers: one at the beginning, another at the end
        beg, end = 0, len(s)-1
        # Terminating case: start ptr = end ptr
        while beg < end:
            begIsAlphanumeric = s[beg].isalnum()
            endIsAlphanumeric = s[end].isalnum()
            
            # both characters being pointed to are alphanumeric
            if (begIsAlphanumeric and endIsAlphanumeric):
                # iterate and compare characters as you go 
                if(s[beg] == s[end]):
                    beg, end = beg + 1, end - 1
                else:
                    # character that is not equal, the word is not a valid palindrome
                    return False
            # move both pointers if both characters are not alphanumeric
            elif(not begIsAlphanumeric and not endIsAlphanumeric):
                beg, end = beg + 1, end - 1
            # move only the pointer for the character that is not alphanumeric
            elif(not begIsAlphanumeric): beg = beg + 1
            # the end ptr must be non-alphanumeric if previous cases did not pass
            else: end = end -1
            
        # successfully iterated through string means it's a valid palindrome
        return True


# Test Cases
# "A man, a plan, a canal: Panama" -> true
# "race a car" -> false
# "" -> false
# " " -> true
# "  nurses run     " -> true