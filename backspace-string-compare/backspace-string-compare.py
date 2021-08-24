class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stk1 = []
        stk2 = []
        for c in s:
            if c!='#':
                stk1.append(c)
            elif c=='#' and stk1:
                stk1.pop()
                
        for c in t:
            if c!='#':
                stk2.append(c)
            elif c=='#' and stk2:
                stk2.pop()
      
        if stk1==stk2:
            return True
        
        return False