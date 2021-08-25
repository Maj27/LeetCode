class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sol = ''
        if len(s)==0:
            return 0
        
        length = 0
        
        chars = {}
        start = 0
        
        for i in range(len(s)):
            if s[i] in chars and start<= chars[s[i]]:
                start = chars[s[i]] + 1
                
            else:
                if i-start+1>length:
                    length = i-start+1     
                    sol = s[start:i+1]
                
            chars[s[i]]= i    
                     
        return length
                     
  