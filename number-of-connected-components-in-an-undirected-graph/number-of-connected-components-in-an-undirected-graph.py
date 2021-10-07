class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        
        
        def dfs(node):
            for nei in adjList[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        
        # build adjecency list
        adjList = {i:[] for i in range(n)}
        
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
            
        # iterate through list starting from any node,and dfs any connected nodes
        visited = set()
        count=0
        for node in range(n):
            if node not in visited:
                visited.add(node)
                count+=1
                dfs(node)
            
        return count   
            
            
            