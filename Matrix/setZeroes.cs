public class Solution {
    public void SetZeroes(int[][] matrix) {
        if (matrix.Length == 0) return;
        
        int m = matrix.Length;
        int n = matrix[0].Length;
        
        // loop and tag the columns
        List<int> targetCols = new List<int>();
        foreach (var row in matrix)
        {
            for (int col = 0; col < n; col++)
            {
                if (row[col] == 0) targetCols.Add(col);
            }
        }
        
        foreach (var row in matrix)
        {
            // if the row already has 0, set all values in row to 0
            if (row.Contains(0))
            {
                for (int col = 0; col < n; col++)
                {
                    row[col] = 0;
                }
            }
            // set only value at the target column to 0 if 0 is not already in the row
            else
            {
                foreach (var col in targetCols)
                {
                    row[col] = 0;
                }
            }
        }
    }
}