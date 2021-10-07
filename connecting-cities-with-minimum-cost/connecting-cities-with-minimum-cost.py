class Solution(object):
    def minimumCost(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        
        def union(city1,city2):
            #parent[findParent(city2)]=findParent(city1)
            
            root1, root2 = findParent(c1), findParent(c2)
   
            parent[root2] = root1  # Always join roots!
 
            
        def findParent(city):
            if parent[city]!=city:
                parent[city] = findParent(parent[city])
            return parent[city]

        
        #set initial parents
        parent = {i:i for i in range(1,n+1)}

        connections.sort(key = lambda x:x[2])
        totalCost = 0
        
        for c1,c2,cost in connections:
            if findParent(c1)!=findParent(c2):
                totalCost+=cost
                union(c1,c2)
   
        root = findParent(1)
        for p in parent:
            if findParent(p)!=root:
                return -1
            
        return totalCost
                
        
        