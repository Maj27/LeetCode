class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        
        dict_t = Counter(t)
        dict_s = {k:0 for k in dict_t.keys()}
       
        def checkIfContained(dic, tar):
            for k,v in tar.items():
                if dic[k]<v:
                    return False
                
            return True
        
        min_len = len(s)+1
        sol = ''
        l = 0
        
        for r in range(len(s)):
            if s[r] in dict_t:
                dict_s[s[r]]+=1
                
            while checkIfContained(dict_s, dict_t):
                if r-l+1 < min_len:
                    min_len = r-l+1
                    sol = s[l:r+1]
                    
                if s[l] in dict_s:
                    dict_s[s[l]]-=1
                l+=1
            
        
        return sol if min_len<len(s)+1 else ''