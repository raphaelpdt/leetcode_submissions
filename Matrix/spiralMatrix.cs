public class Solution {
    public IList<int> SpiralOrder(int[][] matrix) {
        if (matrix.Length == 1)
        {
            return matrix[0].ToList();
        }
        
        // store the matrix dimensions, this will be used to
        // mark current "first row" and current "last column"
        // for spiral traversal
        int m = matrix.Length;
        int n = matrix[0].Length; // use as marker to determine first col to traverse
        var result = new List<int>();
        
        int i = 0;
        int j = 0;
        while (i < m && j < n)
        {
            // traverse along first row then
            for (int col = j; col < n; col++)
            {
                result.Add(matrix[i][col]);
            }
            i++; // increment "first row"
            
            // go down last column, but stop just before the last row
            for (int row = i; row < m-1; row++)
            {
                result.Add(matrix[row][n-1]);
            }
            n--; // done traversing last col
            
            // go back along last row, but stop just before the first col
            if (i < m)
            {
                for (int col = n; col > j-1; col--)
                {
                    result.Add(matrix[m-1][col]);
                }
                m--; // decrement last row
            }
            
            // go up the first column
            if (j < n)
            {
                for (int row = m-1; row > i-1; row--)
                {
                    result.Add(matrix[row][j]);
                }
                j++; // increment "first col" to traverse up
            }
        }
        
        return result;
    }
}