class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        letters = {}
        for c in s:
            if letters.get(c,0)==0:
                letters[c] = 1
            elif letters.get(c,0)==1:
                letters[c] = 0
        
        count = 0
        for k,v in letters.items():
            if v==1:
                count+=1
                if count>1:
                    return False
        return True