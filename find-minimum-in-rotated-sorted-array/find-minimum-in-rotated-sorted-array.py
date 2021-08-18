class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        l,h = 0, len(nums)-1
       
        while l<h:
            m = (h+l)//2
            
            if nums[m]>nums[h]:
                l=m+1
            
            else:
                h=m
                
        return nums[l]