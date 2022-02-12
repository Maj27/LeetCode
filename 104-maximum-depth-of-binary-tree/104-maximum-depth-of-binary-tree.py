# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root: return res
        q = deque()
        q.append(root)
        
        while q:
            new_q = deque()
            res+=1
            while q:
                node = q.popleft()
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right) 
                    
            q = new_q
            
        return res
                    
        