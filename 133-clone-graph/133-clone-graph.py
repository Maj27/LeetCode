"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None
        
        
        newGraph = {}
        
        def cloneDFS(node):
            
            if node in newGraph:
                return newGraph[node]
            
            newNode = Node(node.val)
            newGraph[node] = newNode
            
            for nei in node.neighbors:
                newNode.neighbors.append(cloneDFS(nei))
            
            return newNode
            
        return cloneDFS(node) 
        
  
    
    
