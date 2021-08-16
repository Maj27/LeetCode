class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        binary = bin(n) #0b11010
        N = len(binary)-2
        ones = '1'* N
        return int(ones,2)^n
        
        