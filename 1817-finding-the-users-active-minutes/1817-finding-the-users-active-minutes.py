class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        ''' time limit 
        mapping = defaultdict(set)
        for log in logs:
            id, minute = log
            mapping[id].add(minute)
	
        UAM = [0 for i in range(k)]
        for key, value in mapping.items():
            if len(value)<=k:
                UAM[len(value)-1]+=1

        return UAM

        '''
        
        mapping = defaultdict(set)
        for log in logs:
            id_, minute = log
            mapping[id_].add(minute)
        
        mapping2 = defaultdict(int)
        for key, value in mapping.items():
            n = len(value)
            mapping2[n]+=1
               
                
        UAM = [0 for i in range(k)]
        for key, value in mapping2.items():
            if key<=k:
                UAM[key-1]+=value

        return UAM
