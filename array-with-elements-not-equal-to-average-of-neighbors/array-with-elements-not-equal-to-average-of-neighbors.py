class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res = []
        l,r = 0, len(nums)-1
        while len(res)!=len(nums):
            res.append(nums[l])
            if l!=r:
                res.append(nums[r])
            l+=1
            r-=1
        return res