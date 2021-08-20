class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        
        max_water = 0
        
        while l<r:
            water = (r-l)*min(height[r],height[l])  
            max_water = max(max_water, water)
            if height[r]<height[l]:
                r=r-1
            else:
                l=l+1
                
        return max_water