class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        N = len(grid[0])
        cumSum1 = grid[0].copy()
        cumSum2 = grid[1].copy()
        
        for i in range(1,N):
            cumSum1[i] += cumSum1[i-1]
            cumSum2[i] += cumSum2[i-1]
        
        res = float('inf')
        
        for i in range(N):
            top = cumSum1[-1]-cumSum1[i]
            bottom = cumSum2[i-1] if i>0 else 0
            
            leftReward = max(top,bottom)
            res = min(leftReward, res)
            
        return res