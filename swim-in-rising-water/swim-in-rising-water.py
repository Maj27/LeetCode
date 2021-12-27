class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        visited = set()
        minHeap = [[grid[0][0], 0, 0]]
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        visited.add((0,0))
        
        while minHeap:
            t,r,c = heapq.heappop(minHeap)
                       
            if r==N-1 and c==N-1:
                return t
            
            for d in directions:
                nr = r+d[0]
                nc = c+d[1]
                
                if not (nr<0 or nc<0 or nr==N or nc==N or (nr,nc) in visited):
                    visited.add((nr,nc))
                    heapq.heappush(minHeap, [max(t,grid[nr][nc]),nr,nc])
        