class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        i = 1
        while i <= n:
            fizz = buzz = False
            
            # set fizz and buzz flags for later check, this
            # also saves from having to redundantly check if
            # i is divisible by 3 and 5
            if i % 3 == 0:
                fizz = True
            
            if i % 5 == 0:
                buzz = True
            
            if fizz or buzz:
                if fizz and not buzz: res.append("Fizz")
                if not fizz and buzz: res.append("Buzz")
                if fizz and buzz: res.append("FizzBuzz")
            else:
                res.append(str(i)) 
            
            i += 1
        
        return res