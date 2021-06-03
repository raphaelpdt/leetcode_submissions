# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # inorder array represents remainder of subtree/children
        # of prev root from the prev call
        if inorder:
            root = preorder.pop(0)
            targetIndex = inorder.index(root)
            res = TreeNode(root)
            
            # recursively build the tree by breaking down the traversals
            # preorder represents the order of nodes, while inorder
            # represents the structure of the tree
            res.left = self.buildTree(preorder, inorder[0 : targetIndex])
            res.right = self.buildTree(preorder, inorder[targetIndex+1 : ])
            
            return res