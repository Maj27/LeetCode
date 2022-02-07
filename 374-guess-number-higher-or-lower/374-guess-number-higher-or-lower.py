# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        l,h=1,n
        m=n//2
        while guess(m):
            m = (l+h)//2
            if guess(m)<0:
                h=m-1
            elif guess(m)>0:
                l=m+1
            
        
        return m
        