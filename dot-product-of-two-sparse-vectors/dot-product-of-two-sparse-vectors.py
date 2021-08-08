class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.vect = {}
        for i in range(len(nums)):
            if nums[i]!=0:
                self.vect[i]=nums[i]
    
    
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        prod = 0
        for i,n in self.vect.items():
            m = vec.vect.get(i,0)
            if n!=0 and m!=0:
                prod += n*m
        
        return prod

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)