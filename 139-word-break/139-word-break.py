class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        wordDict = set(wordDict)
        true = set()
        false = set()
        def checkifexist(st):
            if st in true: return True
            if st in false: return False
            
            if st in wordDict:
                true.add(st)
                return True
            
            for i in range(len(st)):
                left, right = st[:i], st[i:]
                if checkifexist(left) and checkifexist(right):
                    return True
            false.add(st)
            return False
        

        return checkifexist(s)
        '''
        
        dp = [True] + [False]*len(s)
                
        for i in range(1,len(s)+1):
            for w in wordDict:
                if w==s[i-len(w):i] and dp[i-len(w)]:
                    dp[i]=True
                    break
                
        return dp[-1]
        
        