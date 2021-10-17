class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []
        
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.small)<=len(self.large):
            heapq.heappush(self.small, -1*num)
        else:    
            heapq.heappush(self.large, num)
            
        if self.small and self.large and (-1*self.small[0]>self.large[0]):
            s = -1* heapq.heappop(self.small)
            l = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*l)
            heapq.heappush(self.large, s)

    def findMedian(self):
        """
        :rtype: float
        """

        if len(self.small)==0 and len(self.large)==0:
            return []
        if len(self.small)>len(self.large):
            return -1*self.small[0]
        elif len(self.large)>len(self.small):
            return self.large[0]
        else:
            return ((-1 *self.small[0])+ self.large[0])/2.0
       

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()