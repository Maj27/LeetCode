class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        sol = matrix
        res = 0
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if sol[i][j]!=0:
                    sol[i][j]+=min(sol[i-1][j],sol[i][j-1],sol[i-1][j-1])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res+= sol[i][j]
                    
        return res