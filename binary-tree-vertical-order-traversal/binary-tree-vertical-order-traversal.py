# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        sol = []
        dic = {}
        self.minCol,self.maxCol =0,0
        
        def dfs(node, row, col):
            
            if not node:
                return
                
            self.minCol = min(self.minCol,col)
            self.maxCol = max(self.maxCol,col)
            
            if col in dic:
                dic[col].append([row,node.val])
            else:
                dic[col]= [[row,node.val]]
                    
            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)
            
        
        dfs(root,0,0)
        
        for i in range(self.minCol,self.maxCol+1):
            col = sorted(dic[i], key= lambda x:x[0])
            nodes = [n[1] for n in col]
            sol.append(nodes)
        return sol
        