class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        
        N = len(nums)
        leftProd = [0]*N
        rightProd = [0]*N
        
        prod = 1 
        for i in range(N):
            leftProd[i] = prod
            prod = prod *  nums[i]
            
        prod = 1 
        for i in range(N-1,-1,-1):
            rightProd[i] = prod
            prod = prod *  nums[i]

        
        for i in range(N):
            leftProd[i]*=rightProd[i]
            
        return leftProd