class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target>=letters[len(letters)-1]:
            return letters[0]
        
        l,h = 0, len(letters)-1
        
        ind = -1
        while l<h:
            m =(l+h)//2
            if letters[m]>target:
                h = m
            else:
                l = m+1
                
        return letters[h]
    