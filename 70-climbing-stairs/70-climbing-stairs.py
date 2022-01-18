class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1,2]
        
        if n<3:
            return n
        
        n1 = 1
        n2 = 2
        for i in range(n-2):
            s = n1+n2
            n1=n2
            n2=s
            
        return s