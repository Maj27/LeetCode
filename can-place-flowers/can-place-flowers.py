class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        count = 0
        flowerbed = [0] + flowerbed + [0]
        i = 0
        while i <len(flowerbed)-2:
            if flowerbed[i] == flowerbed[i+1] == flowerbed[i+2]== 0:
                count+=1
                i+=2
            else:
                i+=1
        '''
        count = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
        	if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
        		flowerbed[i] = 1
        		count += 1
        return count >= n
        '''
        return count>=n
