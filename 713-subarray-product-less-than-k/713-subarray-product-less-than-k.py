class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1: return 0
        
        prod = 1
        ans = 0
        left = 0
        
        for right, val in enumerate(nums):
            prod*=val
            while prod>=k:
                prod/=nums[left]
                left+=1
            ans+= (right-left+1)
        
        return ans
