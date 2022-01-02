class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        i = len(nums)-1
        l,r = 0,len(nums)-1
        
        while i>=0:
            if abs(nums[r])>abs(nums[l]):
                res[i]=nums[r]**2
                r-=1 
            else:
                res[i]=nums[l]**2
                l+=1
            i-=1
        
        return res
        
        