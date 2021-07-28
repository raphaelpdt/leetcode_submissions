class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        n = len(matrix[0]) # store value of row length
        for row in matrix:
            # do Binary Search per row
            if self.binarySearch(row, n, target):
                return True
            
        return False
    
    def binarySearch(self, row, rowLength, target):
        """
        :type row: List[int]
        :type rowLength: int
        :type target: int
        :rtype: bool
        """
        beg, end = 0, rowLength - 1
        while (beg <= end):
            mid = (beg + end) / 2
            
            if row[mid] == target:
                return True
            elif row[mid] > target:
                end = mid-1
            else:
                beg = mid+1
        
        return False