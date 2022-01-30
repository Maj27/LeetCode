class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        
        def dfs(r, c, visited, prevHeight):
            if (r, c) in visited or \
                r<0 or c<0 or r==ROWS or c==COLS or \
                heights[r][c] < prevHeight:
                    return
            visited.add((r,c))
            for i,j in directions:
                dfs(r+i, c+j, visited, heights[r][c])
                
        #add first row and col to pacific
        for c in range(COLS):# row 0
            dfs(0, c, pacific, heights[0][c])
        for r in range(ROWS): #col 0 
            dfs(r, 0, pacific, heights[r][0])
        
        #add last row and col to atlantic
        for c in range(COLS):# row n-1
            dfs(ROWS-1,c, atlantic, heights[ROWS-1][c])
        for r in range(ROWS): #col m-1 
            dfs(r,COLS-1, atlantic, heights[r][COLS-1])
              
                        
        # now check if each cell in both add to sol
        sol = []
        
        for (r,c) in pacific:
            if (r,c) in atlantic:
                    sol.append([r,c])
             
        return sol
        