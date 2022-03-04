# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        
        def dfs(node, bound):
            if not node:
                return 
            if node.val>=bound:
                self.ans+=1
            dfs(node.left, max(bound, node.val))
            dfs(node.right, max(bound, node.val))
        
        dfs(root, root.val)
        return self.ans