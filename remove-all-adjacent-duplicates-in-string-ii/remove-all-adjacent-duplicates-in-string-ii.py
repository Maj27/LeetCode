class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = []
        i = 0
        
        for c in s:
            if res and res[-1][0]==c:
                res[-1][1]+=1
            else:
                res.append([c,1])
                
            if res[-1][1]==k:
                res.pop()

        return ''.join([c[0]*c[1] for c in res])
