class solution(object):
    def largestK(A):
        ## PSEUDOCODE / BRAINSTORMING ##
        # sort the array
        # init var to hold result
        # int vars to point to left and right of sorted A
        # while left < right
            # flip the bit on the number at the left ptr
            # update res to be max of left or res if left == right
            # increment left if number at left is less than beginning
            # decrement right if number at left is less than at the right
        
        if len(A) == 1: return 0
        
        A = sorted(A)
        res = 0
        left, right = 0, len(A) - 1
        while left < right:
            if A[left] < 0:
                curr_left, curr_right = A[left] * -1, A[right]
                
                if curr_left == curr_right:
                    res = max(res, curr_left)
                    left += 1
                    right -= 1
                elif curr_left < curr_right:
                    right -= 1
                else:
                    left += 1
            else:
                break # if left pointer does not point to a neg val, there are no other K's to find
        
        return res
    
    # Time Complexity: (O n log n), the sorting is the most expensive step. The while loop will be O(log n)
    print(largestK([3,2,-2,5,-3])) # expect 3
    print(largestK([1,2,3,-4])) # expect 0
    print(largestK([2,-2])) # expect 2
    print(largestK([1])) # expect 0
    print(largestK([1,-2])) # expect 0
    print(largestK([2,2])) # expect 0