class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        baloon = {c: 0 for c in 'balloon'}
        
        for c in text:
            if c in baloon:
                baloon[c]+=1
        baloon['o']=baloon['o']//2
        baloon['l']=baloon['l']//2
        return min(baloon.values()) if len(baloon)==5 else 0
