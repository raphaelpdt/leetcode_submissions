class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        m, n = len(matrix), len(matrix[0]) # store value of col length and row length
        row, col = 0, n-1
        
        # row and col will each represent the beg and end markers in binary search
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                # search an earlier column if curr coordinates are greater than target
                col -= 1
            else:
                # search a later row if target is greater than value at curr location
                row += 1
        
        return False