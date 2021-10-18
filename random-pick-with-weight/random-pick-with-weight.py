class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        s = 0
        self.cumSum = [0]*len(w)
        for i in range(len(w)):
            s+=w[i]
            self.cumSum[i] = s 

    def pickIndex(self):
        """
        :rtype: int
        """
        
        def binarySearch(val):
            l,r=0,len(self.cumSum)-1 
            while l<r:
                mid = (l+r)//2
                if val>self.cumSum[mid]:
                    l=mid+1
                else:
                    r=mid
            return l
        
        ind = random.randint(1,self.cumSum[-1])
        return binarySearch(ind)
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()