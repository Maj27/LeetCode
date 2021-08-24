class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        freq = [0,0,0]
        i,j = 0,len(nums)-1
        for n in nums:
            freq[n]+=1
        
        i = 0
        while i<freq[0]:
            nums[i] = 0
            i+=1
        tmp= i
        while i<tmp+freq[1]:
            nums[i] = 1
            i+=1
        tmp= i
        while i<tmp+freq[2]:
            nums[i] = 2
            i+=1

            
   