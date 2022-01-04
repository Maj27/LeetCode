class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)
        for i,n in enumerate(nums):
            ans = ans^i^n
        
        return ans
        ''' 
        i = 0
        while i<len(nums):
            if  nums[i]<len(nums) and nums[i]!=nums[nums[i]]:
                nums[i],nums[nums[i]] = nums[nums[i]],nums[i]
            else:
                i+=1
                
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        
        return len(nums)
        '''
    
        
    
        