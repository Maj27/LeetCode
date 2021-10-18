class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        def _reverse(low, high):
            while low < high:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1

                
        flag = False
        n = len(nums)-1
        for i in range(n,0,-1):
            if nums[i]>nums[i-1]:
                smallest_ind = i-1
                flag= True
                break

        if flag:
            for i in range(n,smallest_ind,-1):
                if nums[i]>nums[smallest_ind]:
                    mx_ind = i
                    break

            nums[smallest_ind],nums[mx_ind ] = nums[mx_ind ],nums[smallest_ind]
            _reverse(smallest_ind+1,n) 
        
        else:
            _reverse(0, n)