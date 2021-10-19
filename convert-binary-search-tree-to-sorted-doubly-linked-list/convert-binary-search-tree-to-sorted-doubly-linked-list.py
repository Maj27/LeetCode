"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        self.head, self.tail = None, None

        def dfs(node):
            
            if not node:
                return 
            
            dfs(node.left)
            
            if self.tail:
                self.tail.right =node
                node.left = self.tail
            else:
                self.head = node
                
            self.tail = node
            
            dfs(node.right)
            
       
        if not root:
            return 
                
        dfs(root)
        
        self.head.left = self.tail
        self.tail.right = self.head
        
        return self.head
            
            
            
            
        