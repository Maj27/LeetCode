class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        heapq.heapify(heap)
        
        for e in nums:
            if len(heap)>=k:
                heapq.heappush(heap,e)
                heapq.heappop(heap) 
            else:
                heapq.heappush(heap,e)
                
        return heapq.heappop(heap)
                