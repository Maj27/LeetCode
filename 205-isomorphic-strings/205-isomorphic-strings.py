class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        def checkMapping(st1, st2):
            mapping = {}
            
            for a,b in zip(st1,st2):
                if a not in mapping:
                    mapping[a] = b
                else:
                    if mapping[a]!=b:
                        return False
       
            return True
            
        return checkMapping(s, t) and checkMapping(t, s)