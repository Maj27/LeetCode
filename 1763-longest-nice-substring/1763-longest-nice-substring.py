class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def niceSubstring(st):
            if len(st)<2:
                return ''
            
            chars = set(st)
            for i in range(len(st)):
                if not(st[i].lower() in chars and st[i].upper() in chars):
                    left = niceSubstring(st[:i])
                    right = niceSubstring(st[i+1:])
                    
                    return left if len(left)>=len(right) else right
            return st
        
        return niceSubstring(s)
                    