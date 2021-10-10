class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.unique = {}
        self.q = deque(nums)
        self.front = 0

        for n in nums:
            self.unique[n] = self.unique.get(n,0)+1
            
            
    def showFirstUnique(self):
        """
        :rtype: int
        """
        while self.front<len(self.q):
            if self.unique[self.q[self.front]]==1:
                return self.q[self.front]
            self.front+=1
        
        return -1
                
    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.q.append(value)
        self.unique[value] = self.unique.get(value,0)+1
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)