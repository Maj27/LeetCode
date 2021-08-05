class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        rooms = 0
        if len(intervals)==1:
            return 1
        
        start = sorted([x[0] for x in intervals])
        end = sorted([x[1] for x in intervals])
        
        i ,j = 0,0
        print(start)
        print(end)
        tmp = 0
        while i<len(start):
            if start[i]<end[j]:
                i+=1
                tmp+=1
                rooms = max(rooms,tmp)
            else:
                j+=1
                tmp-=1
            
            
        return rooms
            