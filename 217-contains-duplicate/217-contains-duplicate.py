class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = {}
        for n in nums:
            if n in unique:
                return True
            unique[n]=1
        
        return False