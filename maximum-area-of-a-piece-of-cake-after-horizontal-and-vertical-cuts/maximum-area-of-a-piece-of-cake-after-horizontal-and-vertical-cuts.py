class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """        
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        
        max_h = 0
        max_v = 0
        
        for i in range(1,len(horizontalCuts)):
            h = horizontalCuts[i] -horizontalCuts[i-1]
            max_h = max(max_h,h)
        for j in range(1,len(verticalCuts)):
            v = verticalCuts[j] -verticalCuts[j-1]
            max_v = max(max_v,v)
                                  
        max_area = (max_h*max_v)%(10**9+7)
                
        return max_area