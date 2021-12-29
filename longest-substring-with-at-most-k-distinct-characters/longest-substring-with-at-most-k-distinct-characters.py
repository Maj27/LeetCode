class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        dic = {}
        start,end = 0,0 
        maxLen = 0
        
        while end<len(s):
            dic[s[end]] = end
            if len(dic)>k:
                minVal = min(dic.values())
                del dic[s[minVal]]
                start=minVal+1
            maxLen = max(maxLen, end-start+1)
            end+=1
            
        return maxLen
