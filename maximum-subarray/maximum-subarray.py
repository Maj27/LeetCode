class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        if you can modify nums:
        
        for i in range(1,len(nums)):
            if nums[i-1]>0:
                nums[i]+=nums[i-1]
                
        return max(nums)
        """
        
        max_sub = nums[0]
        curr_sum = 0
        
        for n in nums:
            if curr_sum<0:
                curr_sum = 0
            curr_sum += n
            
            max_sub = max(max_sub, curr_sum)
        return max_sub
        
