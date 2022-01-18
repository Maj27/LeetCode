class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1,2]
        
        if n<=3:
            return n
        
        s = 2
        while s<n:
            moves = steps[s-2]+steps[s-1]
            steps.append(moves)
            s+=1
            
        return steps[-1]