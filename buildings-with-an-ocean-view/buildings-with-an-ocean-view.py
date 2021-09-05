class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        mx = heights[-1]
        res = [len(heights)-1]
        
        for i in range(len(heights)-2,-1,-1):
            if heights[i]>mx:
                res.append(i)
                mx = heights[i]
                
        return res[::-1]
    
