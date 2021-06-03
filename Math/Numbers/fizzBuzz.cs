public class Solution
{
    public IList<string> FizzBuzz(int n)
    {
        List<string> res = new List<string>();
        int i = 1;
        while (i <= n)
        {
            // re-init bool vars at each iteration
            bool fizz = false;
            bool buzz = false;

            // set fizz and buzz flags for later check, this
            // also saves from having to redundantly check if
            // i is divisible by 3 and 5
            if (i % 3 == 0) fizz = true;
            if (i % 5 == 0) buzz = true;

            if (!fizz && !buzz)
                res.Add(i.ToString());
            else
            {
                if (fizz && buzz) res.Add("FizzBuzz");
                // if above case is not satisfied, only one of
                // fizz or buzz are true.
                else if (fizz) res.Add("Fizz");
                else if (buzz) res.Add("Buzz");
            }

            i++;
        }

        return res;
    }
}