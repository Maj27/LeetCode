class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        #xor represent the sum
        # & takes care of the carry
        
        # The first step is to manually bound the length of sum and carry by setting up a mask 0xFFFFFFFF. & this mask with an (very long) integer will only keep the last 32 bits. Then, at each step of the loop, we & sum and carry with this mask, and eventually carry will be wiped out once it goes beyond 32 bits.
        mask = 0xffffffff
        while b:
            xor = (a^b)&mask
            carry = (a&b)&mask
        
            a = xor
            b = carry<<1
        
        if (a>>31) & 1: # If a is negative in 32 bits sense
			return ~(a^mask)

        return a

        