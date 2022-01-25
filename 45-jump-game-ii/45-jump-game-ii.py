class Solution:
    def jump(self, nums: List[int]) -> int:
        
        ''' Time lime exceeded
        self.sol = len(nums)+1
        def backtrack(i, jumps):        
            if i>=len(nums)-1:
                self.sol = min(self.sol, jumps)
                return
            if nums[i]==0:
                return
            
            jumps+=1
            for j in range(1,nums[i]+1):
                backtrack(i+j, jumps)
                
        
        backtrack(0,0)
        return self.sol 
        '''
        
        # BFS
        jumps = 0
        l=r=0
    
        while r<len(nums)-1:
            furthest = l
            for i in range(l,r+1):
                furthest = max(furthest, i+nums[i])
            
            l = r+1
            r = furthest
            jumps+=1
            
        return jumps
        
                
                
                
                
                
        