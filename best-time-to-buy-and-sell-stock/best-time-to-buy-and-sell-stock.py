class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        '''
        max_prof = 0
        min_= prices[0]
        
        for p in prices:
            if p<min_:
                min_ = p
            else:
                if p-min_ > max_prof:
                    max_prof = p-min_
        
        return max_prof
    
        '''
        max_prof = 0
        min_price = prices[0]
        
        for price in prices:
            min_price = min(min_price, price)
            max_prof = max(max_prof,price-min_price)
        return max_prof