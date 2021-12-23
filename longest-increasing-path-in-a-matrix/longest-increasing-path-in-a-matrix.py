class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        #https://www.youtube.com/watch?v=wCc_nd-GiEc&ab_channel=NeetCode
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {} #(r,c): LIP
        
        def dfs(r, c, val):
            if r<0 or r==ROWS or c<0 or c ==COLS or matrix[r][c]<=val:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            
            directions = [[-1,0],[1,0],[0,-1],[0,1]]
            mx = 0
            for d in directions:
                mx = max(mx, 1+ dfs(r+d[0],c+d[1],matrix[r][c]))
            
            dp[(r,c)] = mx
            return mx
            
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, -1)
                
        return max(dp.values())
            
                
        