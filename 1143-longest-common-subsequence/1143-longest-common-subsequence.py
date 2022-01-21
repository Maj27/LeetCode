class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)+1
        cols = len(text2)+1
        matrix = [[0 for i in range(cols)] for j in range(rows)]
        
        for i in range(1,rows):
            for j in range(1,cols):
                if text1[i-1]==text2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]+1
                else:
                    matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])
        return matrix[-1][-1]