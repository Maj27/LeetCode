# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [float('inf')]
        mn = root.val
        self.dfs(root.left, ans, mn)
        self.dfs(root.right, ans, mn)
        
        return ans[0] if ans[0]<float('inf') else -1
        
    def dfs(self, root, ans, mn):
            if not root or root.val<mn:
                return 
          
            if ans[-1]>root.val>mn:
                ans[-1] = root.val
                 
            self.dfs(root.left, ans, mn)
            self.dfs(root.right, ans, mn)

           
            
            
            