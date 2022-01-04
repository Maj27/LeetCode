class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = ones = twos = 0
        for n in nums:
            if n==0: zeros+=1
            elif n==1: ones+=1
            else: twos+=1
        
        for i in range(zeros):
            nums[i]=0
        for i in range(zeros,zeros+ones):
            nums[i]=1
        for i in range(zeros+ones,zeros+ones+twos):
            nums[i]=2
            