# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.diff = float('inf')
        
        if not root:
            return 
        
        self.sol = root.val
        
        def dfs(node,target):
            if not node:
                return

            new_diff = abs(node.val-target)
            if new_diff<self.diff:
                self.diff = new_diff
                self.sol = node.val
                
            dfs(node.left,target)
            dfs(node.right,target)
                        
        
        dfs(root, target)
        return self.sol
            