class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        if nums[0]==0 and len(nums)>1: return False
        for i in range(1,len(nums)):
            nums[i] = max(nums[i],nums[i-1]-1)
            if nums[i]==0 and i!=len(nums)-1:
                return False
        return True
        '''
        
        jumps = 1
        
        for i in range(len(nums)):
            jumps = max(nums[i], jumps-1)
            if jumps==0 and i!=len(nums)-1:
                return False
        return True
        