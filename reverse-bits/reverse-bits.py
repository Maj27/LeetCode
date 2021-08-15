class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # 1101
        res = 0
        for i in range(32):
            bit = (n>>i)&1
            res = res|(bit<<(31-i))
            
        return res
        
        #  i = 0
        # take 0th index bit (by anding with 1) and add it to the 31th index of res
        # i = 1
        # take 1th index bit and add it to the 30th index of res
        # i = 2
        # take 2th index bit and add it to the 29th index of res,, and so on