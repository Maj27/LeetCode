class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        dic = {}
        for i in range(len(nums)-2):
            j=i+1
            k= len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]>0:
                    k-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
                else:
                    
                    if not (nums[i],nums[j]) in dic:
                        dic[(nums[i],nums[j])]=nums[k]
                        ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                
        return ans
        