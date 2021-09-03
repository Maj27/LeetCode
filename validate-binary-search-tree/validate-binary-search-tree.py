# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root,lBound,rBound):
            if not root:
                return True
            if not (root.val>lBound and root.val< rBound):
                return False
            return (dfs(root.left,lBound,root.val) and dfs(root.right,root.val,rBound))
        
        return dfs(root,float("-inf"),float("inf"))