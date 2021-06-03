"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return node
        
        queue = deque()
        clone = {node: Node(node.val)} # create clone graph as a dict of nodes
        
        queue.append(node)
        # Use a BFS traversal
        while queue:
            curr = queue.popleft()
            
            for neighbor in curr.neighbors:
                # add neighbor node to cloned graph and add to queue
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                # add the curr node to the neighbor's nodes
                clone[neighbor].neighbors.append(clone[curr])
                
        return clone[node] # return cloned graph pointing to root node