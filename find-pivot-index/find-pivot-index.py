class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lSum = 0
        rSum = sum(nums[1:])
               
        for i in range(len(nums)-1):
            if lSum==rSum:
                return i
            lSum+=nums[i]
            rSum-=nums[i+1]
        
        return len(nums)-1 if lSum==rSum else -1
        

        
        