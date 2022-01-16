class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = nums[0]
        maxProd = minProd = 1
        
        for n in nums:
            values = [n, n*minProd, n*maxProd]
            maxProd = max(values)
            minProd = min(values)
            res = max(maxProd, res)
            
        return res
            
            
            
        