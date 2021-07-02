public class Solution
{
    public IList<int> GetRow(int rowIndex)
    {
        var triangle = new List<IList<int>>();

        var firstRow = new List<int> { 1 };
        if (rowIndex == 0)
            return firstRow;
        triangle.Add(firstRow);

        var secondRow = new List<int> { 1, 1 };
        if (rowIndex == 1)
            return secondRow;
        triangle.Add(secondRow);

        for (int i = 2; i <= rowIndex; i++)
        {
            var currRow = new List<int>();

            for (int k = 0; k <= i; k++)
            {
                if (k == 0 || k == i)
                {
                    currRow.Add(1);
                }
                else
                {
                    var prevRow = triangle[i - 1];
                    currRow.Add(prevRow[k - 1] + prevRow[k]);
                }
            }

            triangle.Add(currRow);
        }

        return triangle[rowIndex];
    }
}