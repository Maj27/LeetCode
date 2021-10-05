class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
               
        visited = set()
        provinces = 0
        
        def dfs(node):
            for j in range(len(isConnected)):
                if isConnected[node][j]==1 and j not in visited:
                    visited.add(j)
                    dfs(j)
                
                
        for i in range(len(isConnected)):
            if i not in visited:
                visited.add(i)
                provinces+=1
                dfs(i)
        
        return provinces