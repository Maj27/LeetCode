class Solution(object):
    def getFood(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        #add start to q
        #while q
        #keep poping if #found return count
        # if O and not seen check connected cells if reachable add to new_q and increase count
        # update my q to new_q
        #if iterate thou all return -1
        
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='*':
                    q.append((i,j))
                    visited.add((i,j))
                    break
        
        count = 0            
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        while q:
            new_q = deque()
            while q:
                r,c = q.popleft()
                if grid[r][c]=='#':
                    return count
                     
                for d in directions:
                    nr,nc = r+d[0],c+d[1]
                    if nr>=0 and nr<rows and nc>=0 and nc<cols and (nr,nc) not in visited and grid[nr][nc]!='X':
                        visited.add((nr,nc))
                        new_q.append((nr,nc))
            count+=1  
            q = new_q
            
        return -1
            
            
        
        
        