public class Solution
{
    public IList<IList<int>> Generate(int numRows)
    {
        var res = new List<IList<int>>();
        if (numRows == 0) return res;

        // BASE Cases: if numRows is 1 or 2, return immediately after adding
        // the row
        res.Add(new List<int> { 1 });
        if (numRows == 1) return res;

        res.Add(new List<int> { 1, 1 });
        if (numRows == 2) return res;

        for (int i = 2; i < numRows; i++)
        {
            List<int> newRow = new List<int>();
            int currEntry = 0;
            while (currEntry <= i)
            {
                if (currEntry == 0 || currEntry == i)
                    newRow.Add(1); // add 1 to first and last entry of the row
                else
                {
                    var prevRow = res[i - 1];
                    newRow.Add(prevRow[currEntry - 1] + prevRow[currEntry]);
                }

                currEntry++;
            }

            res.Add(newRow);
        }

        return res;
    }
}