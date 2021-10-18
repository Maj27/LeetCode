class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {0:-1}
        mod = 0
        for i, n in enumerate(nums):
            if k != 0:
                mod = (mod + n) % k
            else:
                mod += n
            if mod in dic:
                if i - dic[mod] >= 2:
                    return True
            else:
                dic[mod] = i
        return False
