class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
                
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        
        minRooms = 0
        curRooms = 0
        s,e = 0,0
        while s<len(start): 
            if start[s]<end[e]:
                curRooms+=1
                s+=1
            else:
                curRooms-=1
                e+=1
            
            minRooms = max(minRooms,curRooms)
            
        return minRooms
                
