class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.vec = {}
        for i in range(len(nums)):
            self.vec[i]=nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        dot = 0
        for k,v in self.vec.items():
            if k in vec.vec:
                dot+= v*vec.vec[k]
        return dot
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)