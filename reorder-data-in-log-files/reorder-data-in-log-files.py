class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        #initilizat two arrays digs = [] and lets = []
        #iterate
        #if digits (check last char) append to dig[]
        #if letter add [id][rest]
        #sort lets by second [rest] lambda x:x[1]
        #append digs to lets
        
      
            
        
        digits = []
        letters = []
		# divide logs into two parts, one is digit logs, the other is letter logs
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
                
        letters.sort(key = lambda x: x.split()[0])
        letters.sort(key = lambda x: x.split()[1:])           
        result = letters + digits                                 
        return result