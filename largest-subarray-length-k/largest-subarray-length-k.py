class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        sol = nums[0:k]
        for i in range(1,len(nums)-k+1):
            s = 0
            for j in range(i,i+k):
                if nums[j]<sol[s]:
                    break
                elif nums[j]>sol[s]:
                    sol = nums[i:i+k]
                    break
                else:
                    continue
                s+=1
                
        return sol
                