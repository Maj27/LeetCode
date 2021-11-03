class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        result = []
        products.sort()
        
        for i in range(len(searchWord)):
            tmpResult = []
            for product in products:
                if product.startswith(searchWord[:i+1]):
                    tmpResult.append(product)
   
            result.append(tmpResult[:3])
            products = tmpResult
        
        return result