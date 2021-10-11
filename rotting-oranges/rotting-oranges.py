class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows= len(grid)
        cols= len(grid[0])
        
        fresh = 0
        rotten = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    rotten.append((i,j))
        
        if fresh==0:
            return 0
        
        t = 0
        while rotten:
            directions = [[-1,0],[1,0],[0,-1],[0,1]]
            new_q = deque()
            while rotten:
                r,c = rotten.popleft()
                
                for d in directions:
                    nr, nc = r+d[0],c+d[1]
                    if nr>=0 and nr<rows and nc>=0 and nc<cols and grid[nr][nc]==1:
                        new_q.append((nr,nc))
                        grid[nr][nc]=2
                        fresh-=1
                
            t+=1
            rotten = new_q
        
        
        if fresh==0:
            return t-1
        return -1
        