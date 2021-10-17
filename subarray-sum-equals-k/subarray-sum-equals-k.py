class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        cumSum = {0: 1}
        s = 0

        for v in nums:
            s+=v
            
            if s-k in cumSum:
                count = count + cumSum[s-k]
                
            cumSum[s] = cumSum.get(s,0)+1
   
        return count
    
    
       