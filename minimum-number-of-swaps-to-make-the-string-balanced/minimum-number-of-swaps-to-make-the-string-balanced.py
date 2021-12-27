class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        # https://www.youtube.com/watch?v=3YDBT9ZrfaU&ab_channel=NeetCode
        
        mx,close = 0,0
        
        for c in s:
            if c == ']':
                close+=1
            else:
                close-=1
            mx = max(mx,close)
            
        return (mx+1)//2