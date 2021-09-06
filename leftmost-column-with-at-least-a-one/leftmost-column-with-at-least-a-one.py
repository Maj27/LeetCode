# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row, col):
#        """
#        :type row : int, col : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        
        rows, cols = binaryMatrix.dimensions()
        end = cols
        
        for row in range(rows):
            #binary search within row
            l = 0
            r = end
            while l<r:
                col =(l+r)//2
                if binaryMatrix.get(row,col)==1:
                    r = col
                else:
                    l=col+1
                    
            ind = l
            end = ind
        
        
        return ind if ind<cols else -1