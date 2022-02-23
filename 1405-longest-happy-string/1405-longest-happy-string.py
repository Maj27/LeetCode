class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        chars = {'a':a, 'b':b , 'c':c}
        string = ''
        maxHeap = []
        for char,count in chars.items():
            if count:
                heapq.heappush(maxHeap, (-count, char))
      

        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            
            if len(string)>1 and string[-1]==string[-2]==char:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                count2+=1
                string += char2
                    
                if count2:
                    heapq.heappush(maxHeap, (count2, char2))
            else:
                string += char
                count+=1
            
            if count:
                heapq.heappush(maxHeap, (count, char))
                    
            
            
        return string
