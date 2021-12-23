class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #n= window size
        #https://www.youtube.com/watch?v=MOeuK6gaC2A&ab_channel=NeetCode
        n = len(s)
        s += s
        
        alt1, alt2 = '',''
        for i in range(len(s)):
            alt1+='0' if i%2 else '1'
            alt2+='1' if i%2 else '0'
            
        res = n
        diff1,diff2 = 0,0
        
        l=0
        for r in range(len(s)):
            if alt1[r]!=s[r]:
                diff1+=1
            if alt2[r]!=s[r]:
                diff2+=1
            
            if r-l+1>n:
                if alt1[l]!=s[l]:
                    diff1-=1
                if alt2[l]!=s[l]:
                    diff2-=1
                l+=1
                res = min(res, diff1, diff2)
                
        return res