class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        
        N = len(nums)
        sol = [0]*N
        
        prod = 1 
        for i in range(N):
            sol[i] = prod
            prod = prod *  nums[i]
            
        prod = 1 
        for i in range(N-1,-1,-1):
            sol[i] = prod * sol[i]
            prod = prod *  nums[i]

                  
        return sol