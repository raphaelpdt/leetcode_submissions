# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTreeDFS(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # BASE CASE: two empty trees are equal OR reached end of a branch
        if not p and not q: return True 
        # BAS CASE: if one tree is empty and another isn't they are not equal, equiv. to p XOR q
        if (not p and q) or (p and not q): return False 
        
        # only traverse further if nodes have equal vals
        if p.val == q.val:
            # traverse down left subtree, then right subtree. If both trees are equal,
            # they will both return True when they hit the base case
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False # trees are not equal if nodes don't have the same value at any point

    def isSameTreeBFS(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # BASE CASE: two empty trees are equal OR reached end of a branch
        if not p and not q: return True 
        # if one tree is empty and another isn't they are not equal, equiv. to p XOR q
        if (not p and q) or (p and not q): return False
        
        # use queues to facilitate BFS traversal
        pQ = qQ = deque()    
        # add root to queues
        pQ.append(p)
        qQ.append(q)
        while pQ and qQ:
            curr_p, curr_q = pQ.popleft(), qQ.popleft()
            p_left, q_left = curr_p.left, curr_q.left # vars to hold left children
            p_right, q_right = curr_p.right, curr_q.right # vars to hold right children
            
            if curr_p.val != curr_q.val:
                return False # trees are not similar if nodes are not equal at any point
            else:
                # add left children
                if p_left and q_left: 
                    pQ.append(p_left)
                    qQ.append(q_left)
                # curr_p.left XOR curr_q.left
                elif (not p_left and q_left) or (p_left and not q_left):
                    return False # trees are not equal if not structurally similar
                    
                # add right children
                if p_right and q_right: 
                    pQ.append(p_right)
                    qQ.append(q_right)
                # curr_p.right XOR curr_q.left
                elif (not p_right and q_right) or (p_right and not q_right):
                    return False # trees are not equal if not structurally similar
                    
        return True
        
# source for XOR: https://stackoverflow.com/questions/432842/how-do-you-get-the-logical-xor-of-two-variables-in-python