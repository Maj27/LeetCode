class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
       
    
        # 1001
        # 1000
        # 1000
        
        # 1000
        # 0111
        # 0000
        
        # recurseive
        if not n: return 0
        if n==1: return 1
        return 1+self.hammingWeight(n&(n-1))
        

        