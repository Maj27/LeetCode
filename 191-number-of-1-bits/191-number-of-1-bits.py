class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        count = 0
        while n:
            count+=n%2
            n=n>>1
        
        return count
        '''
        #bit manipulation https://www.youtube.com/watch?v=5Km3utixwZs&ab_channel=NeetCode
        count = 0
        while n:
            count+=1
            n = n&(n-1)
        
        return count