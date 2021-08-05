class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        oldColor = image[sr][sc]
        if oldColor ==newColor:
            return image
        self.helper(image, sr, sc, oldColor, newColor)
        return image

    def helper(self,img, r,c, oldColor, newColor):
        img[r][c] = newColor 
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        for d in directions:
            if r+d[0]>=0 and r+d[0]<len(img) and c+d[1]>=0 and c+d[1]<len(img[0]) and img[r+d[0]][c+d[1]] == oldColor:
                self.helper(img,r+d[0], c+d[1],oldColor, newColor)
