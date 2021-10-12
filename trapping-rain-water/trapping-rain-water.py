class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        l,r = 0,len(height)-1
        maxLeft = height[l]
        maxRight = height[r]
        total = 0
        i = 0
        while l<r:
            if maxLeft<maxRight:
                l+=1
                maxLeft = max(maxLeft,height[l])        
                total+= maxLeft- height[l]
            else:
                r-=1
                maxRight = max(maxRight,height[r])                
                total+= maxRight- height[r]
     
        return total