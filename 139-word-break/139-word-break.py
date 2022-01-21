class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
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