class Solution:
    def reorganizeString(self, s: str) -> str:
        # https://www.youtube.com/watch?v=2g_b1aYTHeg&ab_channel=NeetCode
        count = Counter(s)
        
        maxHeap = [(-v,c) for c,v in count.items()]
        heapq.heapify(maxHeap)
        res = ''
        prev = None
        
        while maxHeap or prev:
            if prev and not maxHeap:
                return ''
            
            v,c = heapq.heappop(maxHeap)
            res+=c
            v+=1
            
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if v:
                prev = (v,c)
                
            
        return res
           
            