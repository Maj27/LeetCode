class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        
        if not prices:
            return 0
        
        buyPrice = prices[0]
        
        for price in prices:
            maxProfit = max(maxProfit, price-buyPrice)
            buyPrice = min(buyPrice, price)
            
            
        return maxProfit
    
