class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = float('-inf')
        s = 0
        for i in range(len(nums)):
            s+=nums[i]
            if i>=k-1:
                avg = s/k
                s=s-nums[i-k+1]
                maxAvg = max(avg,maxAvg)
            
        return maxAvg