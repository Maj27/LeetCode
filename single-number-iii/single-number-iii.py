class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        for n in nums:
            xor ^= n
        xor &=-xor # this is to get the right most significant bit of the difference 
        # now the two numbers will fall in two different groups as they have that bit different
        # for other nums, same copies will fall in same group
        # if and this different bit with all numbers you either them in group1 or two, 
        #same nubers will cancel and you end up with the distince ones
        
        groups = [0,0]
        for n in nums:
            if xor&n==0:
                groups[0] = groups[0]^n
            else:
                groups[1] = groups[1]^n
                
        return groups
                
                