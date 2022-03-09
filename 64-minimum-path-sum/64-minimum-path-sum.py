class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        for r in range(1,ROWS):
            grid[r][0] += grid[r-1][0]
        for c in range(1,COLS):
            grid[0][c] += grid[0][c-1]
            
        for r in range(1,ROWS):
            for c in range(1,COLS):
                grid[r][c] += min(grid[r-1][c], grid[r][c-1])
                
        return grid[ROWS-1][COLS-1]