class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        start = '0000'
        if start in deadends:
            return -1
        
        visited = set()
                
        q = deque()
        q.append([start, 0])
        
        def newCombs(comb):
            combs = []
            for i in range(4):
                plus = (int(comb[i])+1)%10
                minus = (int(comb[i])-1+10)%10
                newComb1 = comb[:i] + str(plus) + comb[i+1:]
                newComb2 = comb[:i] + str(minus) + comb[i+1:]
                combs.append(newComb1)
                combs.append(newComb2)
            return combs
        
        while q:
            comb, turns = q.popleft()
            if comb == target:
                return turns
            
            for newComb in newCombs(comb):
                if newComb not in deadends and newComb not in visited:
                    visited.add(newComb)
                    q.append([newComb, turns+1])
        
        return -1
                
                
        
        
        
        
        