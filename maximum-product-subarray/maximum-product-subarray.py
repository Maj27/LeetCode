class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        res = nums[0]
        mx, mn = nums[0], nums[0]
        
        for i in range(1,len(nums)):
            prev_mx = mx
            mx = max(nums[i]*mx, nums[i]*mn, nums[i])
            mn = min(nums[i]*prev_mx, nums[i]*mn, nums[i])
            res = max(res, mx)
 
        return res