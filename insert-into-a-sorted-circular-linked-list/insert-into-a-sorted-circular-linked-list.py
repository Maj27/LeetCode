"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        if not head:
            newNode = Node(insertVal)
            newNode.next = newNode
            return newNode
        
  
        prev = head
        curr = head.next
        
        while True:
            if prev.val<= insertVal and curr.val>=insertVal:
                break
            elif prev.val> curr.val and (insertVal>prev.val or insertVal<curr.val) :
                    break
                
            prev = curr
            curr = curr.next
            
            if prev==head:
                break
        
        newNode = Node(insertVal,curr)
        prev.next = newNode
        
        return head
    
        
