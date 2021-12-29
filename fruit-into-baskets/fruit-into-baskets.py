class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l,r = 0,0
        maxLen = 0
        dic = {}
        
        while r<len(fruits):
            dic[fruits[r]] = r
            if len(dic)==3:
                minVal = min(dic.values())
                l = minVal+1
                del dic[fruits[minVal]]
            maxLen = max(maxLen,r-l+1)    
            r+=1    

        return maxLen