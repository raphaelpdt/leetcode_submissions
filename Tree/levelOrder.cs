/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution
{
    public IList<IList<int>> LevelOrder(TreeNode root)
    {
        List<IList<int>> res = new List<IList<int>>();
        // BASE CASE: empty tree
        if (root == null)
            return res;

        // build a queue to facilitate BFS traversal
        Queue<TreeNode> queue = new Queue<TreeNode>();
        queue.Enqueue(root); // enqueue root node
        // iterate through the queue
        while (queue.Count != 0)
        {
            // keep a count of nodes in the current level
            int levelCount = queue.Count;
            List<int> levelNodes = new List<int>(); // init list for the current level's nodes
            // iterate through all nodes in the current level
            for (int i = 0; i < levelCount; i++)
            {
                TreeNode curr = queue.Dequeue(); // dequeue top node
                levelNodes.Add(curr.val); // add curr node's value to curr level list

                // add any of the node's children
                if (curr.left != null) queue.Enqueue(curr.left);
                if (curr.right != null) queue.Enqueue(curr.right);
            }

            res.Add(levelNodes); // add current leve's nodes to result array
        }

        return res;
    }
}