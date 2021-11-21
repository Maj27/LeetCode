class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits =='': return []
        mapping = {'2':'abc',
                   '3':'def',
                   '4':'ghi',
                   '5':'jkl',
                   '6':'mno',
                   '7':'pqrs',
                   '8':'tuv',
                   '9':'wxyz'}
        sol = []
        
        def backTrack(i,curStr):
            if len(curStr)==len(digits):
                sol.append(curStr)
                return
            
            for c in mapping[digits[i]]:
                backTrack(i+1,curStr+c)
                
                    
        backTrack(0,'')
        return sol