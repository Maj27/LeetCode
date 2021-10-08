class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            comp = target-nums[i]
            if comp in dic:
                return [dic[comp],i]
            dic[nums[i]]=i
                            