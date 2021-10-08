class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        count = 0
        dic = {}
        for i in range(len(time)):
            remainder = time[i]%60
            target = (60-remainder)%60
            if target in dic:
                count+=dic[target]
            dic[remainder]=dic.get(remainder,0)+1
            
        return count

