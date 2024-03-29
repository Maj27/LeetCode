"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        pParents = set()
        qParents = set()
        
        while p:
            pParents.add(p)
            p=p.parent
        
        while q:
            if q in pParents: 
                return q
            q=q.parent