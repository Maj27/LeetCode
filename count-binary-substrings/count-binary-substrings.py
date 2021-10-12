class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr = 1
        prev = 0
        res = 0
        
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                curr+=1
            else:
                res+=min(prev,curr)
                prev = curr
                curr = 1
                
        res+=min(prev,curr)
        return res
                