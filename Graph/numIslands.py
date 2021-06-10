class Solution(object):    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        
        m, n = len(grid), len(grid[0])        
        res = 0 # init var to track count of islands
        for i in range(m):
            for j in range(n):
                # begin counting land iff curr cell is land
                if grid[i][j] == '1':
                    self.countLandDFS(grid, i, j)
                    res += 1
        
        return res
    
    def countLandDFS (self, grid, x, y):
        """
        : type grid: List[List[str]]
        : type x: int
        : type y: int
        : rtype: void
        """
        grid[x][y] = 'v' # mark current node as visited so this won't be counted again
        
        m, n = len(grid), len(grid[0])
        # set of adj coordinates
        xCoords = [0, 1, 0, -1]
        yCoords = [-1, 0, 1, 0]
        for i in range(4):
            adjX, adjY = x + xCoords[i], y + yCoords[i]
            # if curr coordinate is out of bounds or is not land, continue
            if not (0 <= adjX < m) or not (0 <= adjY < n):
                continue
            # continue iff adjacent node is land
            elif grid[adjX][adjY] == '1': 
                self.countLandDFS(grid, adjX, adjY)