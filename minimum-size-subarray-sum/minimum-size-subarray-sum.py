class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        s = 0
        ans = len(nums)+1
        while r<len(nums):
            s+=nums[r]
            while s>=target:
                ans = min(ans, r-l+1)
                s-=nums[l]
                l+=1
                
            r+=1
            
        return ans if ans<=len(nums) else 0 