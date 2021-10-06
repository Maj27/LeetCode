class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        
        """
                    
        dp = [True] + [False]*len(s)
        
        wordDict = set(wordDict)
        
        for i in range(1,len(s)+1):
            for w in wordDict:
                if w==s[i-len(w):i] and dp[i-len(w)]:
                    dp[i]=True
                    break
                
        return dp[-1]
        
     