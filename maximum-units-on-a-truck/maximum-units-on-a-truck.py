class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """

        boxTypes.sort(key=lambda x:x[1],reverse=True)
        maxBoxes = 0
        
        for boxes, units in boxTypes:
            if truckSize>=boxes:
                maxBoxes += boxes*units
                truckSize -= boxes
            else:
                maxBoxes += truckSize*units
                break
        
        return maxBoxes