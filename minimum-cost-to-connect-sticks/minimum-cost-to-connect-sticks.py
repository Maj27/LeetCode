class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """

        if len(sticks) <= 1:
            return 0
        sticks = [s for s in sticks]
        
        heapq.heapify(sticks)
        cost = 0
        
        while len(sticks)>1:
            s1 = heapq.heappop(sticks) 
            s2 = heapq.heappop(sticks) 
            cost+=(s1+s2)
            heapq.heappush(sticks,s1+s2)

        return cost
