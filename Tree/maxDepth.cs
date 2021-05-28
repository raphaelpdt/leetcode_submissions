/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int MaxDepthDFS(TreeNode root) {
        // BASE CASE: reached limit or tree is empty
        if (root == null) return 0;
        
        // create variables that count the length of each subtree,
        // when the recursion comes back to the first call, each 
        // var represents longest subtree of each side
        int leftLen = MaxDepth(root.left);
        int rightLen = MaxDepth(root.right);
        
        return Math.Max(leftLen + 1, rightLen + 1);
    }


    // Source for level count idea: https://stackoverflow.com/questions/31247634/how-to-keep-track-of-depth-in-breadth-first-search 
    public int MaxDepthBFS(TreeNode root)
    {
        if (root == null) return 0;

        int res = 0;
        // build a queue to facilitate BFS traversal of the tree
        Queue<TreeNode> queue = new Queue<TreeNode>();
        queue.Enqueue(root);

        // We will use a level-order traversal and devise a way to keep track
        // of what level we are currently in
        while (queue.Count != 0)
        {
            // Iterate through all nodes in the current level
            int levelCount = queue.Count; // count of all nodes at current level
            for (int i = 0; i < levelCount; i++)
            {
                // remove top node then add any of its children to the queue
                TreeNode curr = queue.Dequeue();
                if (curr.left != null) queue.Enqueue(curr.left);
                if (curr.right != null) queue.Enqueue(curr.right);
            }
            res++; // increment counter when done processing all nodes in curr level
        }

        return res; // loop terminates once all nodes have been processed
    }
}