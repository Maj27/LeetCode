# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
   
        self.index = len(inorder)-1
        inorderIndexMap = {val:ind for ind, val in enumerate(inorder)}
        
        def dfs(leftBount, rightBound):
            if leftBount>rightBound:
                return 
            value = postorder[self.index]
            self.index-=1
            root = TreeNode(value)
            root.right = dfs(inorderIndexMap[value]+1, rightBound)
            root.left = dfs(leftBount, inorderIndexMap[value]-1)
            return root
        
        return dfs(0, len(inorder)-1)