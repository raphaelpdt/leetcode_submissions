class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            coords = [
                (-1, 0), (0, 1), (1, 0), (0, -1)
            ]
            
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] != 1:
                return 0
            
            grid[i][j] = -1 # visit this cell
            x = 1 # begin land count
            for coord in coords:
                nextRow, nextCol = i + coord[0], j + coord[1]
                x += dfs(nextRow, nextCol)
            
            return x
        
        res = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # found an island, run dfs
                if grid[i][j] == 1:
                    # recursively check all adjacent land tiles in this island,
                    # then append land area to result array
                    res.append(dfs(i, j))
        
        return 0 if not res else max(res)
