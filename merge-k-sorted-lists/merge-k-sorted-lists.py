# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
      
        
        heap = []
        
        for head in lists:
            if head:
                heapq.heappush(heap,(head.val,head.next))
                
        head= ListNode(0)
        cur=head
        while heap:
            v,nxt = heapq.heappop(heap)
            node = ListNode(v)
            cur.next= node
            cur = node
            if nxt: 
                heapq.heappush(heap,(nxt.val,nxt.next))
        return head.next

	

