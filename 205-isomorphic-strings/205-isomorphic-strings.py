class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        for a,b in zip(s,t):
            if a not in mapping:
                mapping[a] = b
            else:
                if mapping[a]!=b:
                    return False
        mapping = {}
        for a,b in zip(t,s):
            if a not in mapping:
                mapping[a] = b
            else:
                if mapping[a]!=b:
                    return False
        return True