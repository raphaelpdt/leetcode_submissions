class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## PSEUDOCODE / BRAINSTORMING ##
        # use a dictionary to record each character and their frequency
        # get the list of frequencies and sort them
        # foreach frequency
            # check if neighbor is a duplicate
                # decrement frequency until list of freq no longer contains the entry
        
        freqDict = {}
        # generate counter for this string and its characters
        for c in s:
            if c in freqDict:
                freqDict[c] += 1
            else:
                freqDict[c] = 1
        
        res = 0 # init var to count decrements of a character
        used = set() # init set to keep track of frequencies encountered
        for ch, freq in freqDict.items():
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            used.add(freq) # record occurrence of this freq
        
        return res