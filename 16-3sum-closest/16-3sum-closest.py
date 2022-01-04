class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = nums[0]+nums[1]+nums[2]
        nums.sort()
               
        for i in range(len(nums)-2):
            l=i+1
            r = len(nums)-1
            while l<r:
                s = nums[i]+nums[l]+nums[r]
                if abs(s-target)<abs(res-target):
                    res = s
                if s==target:
                    return s
                elif s>target:
                    r-=1
                else:
                    l+=1
                    
        return res
        
