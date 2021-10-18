class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stck = []
        ans = [0]* n
        
        for log in logs:
            idd, se , t = log.split(':')
            idd = int(idd)

            t = int(t)
            if se=='start':
                if stck:
                    ans[stck[-1]] += t-strt
                    
                strt = t
                stck.append(idd)
          
            else:
                
                ans[stck[-1]] += t-strt+1
                strt = t+1 
                stck.pop()
        
        return ans