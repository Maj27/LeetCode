class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        p = 1
        res = []
        
        for i in range(len(nums)):
            res.append(p)
            p = p*nums[i]
            
        p = 1
        
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i]*p
            p = p*nums[i]
            
        return res
            