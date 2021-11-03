class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda x:x[1],reverse= True)

        i = 0
        ans = 0
        while truckSize >0 and i<len(boxTypes):
            
            q, v = boxTypes[i]
            if q<=truckSize:
                ans+=q*v        
            else:
                ans+=truckSize*v
            truckSize-=q
            i+=1
            
        return ans
            