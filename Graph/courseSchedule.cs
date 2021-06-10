public class Solution
{
    public bool CanFinish(int numCourses, int[][] prerequisites)
    {
        // build dict representation of graph
        Dictionary<int, List<int>> clone = new Dictionary<int, List<int>>();
        foreach (var course in prerequisites)
        {
            int curr = course[0];
            int prerequisite = course[1];
            if (!clone.ContainsKey(curr))
            {
                List<int> prereqs = new List<int> { prerequisite };
                clone.Add(curr, prereqs);
            }
            else
            {
                clone[curr].Add(prerequisite);
            }
        }

        int[] visited = new int[numCourses]; // use for cycle detection
        for (int i = 0; i < numCourses; i++)
        {
            if (!HasCycle(visited, clone, i))
                return false;
        }

        return true;
    }

    public static bool HasCycle(int[] visited, Dictionary<int, List<int>> graph, int node)
    {
        if (visited[node] == 1) return true;
        if (visited[node] == -1) return false;

        visited[node] = -1;
        if (graph.ContainsKey(node))
        {
            foreach (var course in graph[node])
            {
                if (!HasCycle(visited, graph, course))
                    return false;
            }
        }

        // mark node as being part of a cycle
        visited[node] = 1;
        return true;
    }
}