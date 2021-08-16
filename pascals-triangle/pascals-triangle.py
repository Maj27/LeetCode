class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        for i in range(numRows-1):
            tmp = [0]+ res[-1]+ [0]
            new_row = []
            for j in range(len(tmp)-1):
                new_row.append(tmp[j]+tmp[j+1])
            res.append(new_row)
        return res
            

            