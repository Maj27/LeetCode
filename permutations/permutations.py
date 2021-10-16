class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tmp = []
        res = []
        self.dfs(nums,tmp,res)
        
        return res
    
    def dfs(self, nums, tmp, res):
        if len(nums)==1:
            tmp.append(nums[0])
            res.append(tmp)
        
        else:
            for i in range(len(nums)):
                sub = nums[:i]+nums[i+1:]
                self.dfs(sub, tmp + [nums[i]], res)

    
