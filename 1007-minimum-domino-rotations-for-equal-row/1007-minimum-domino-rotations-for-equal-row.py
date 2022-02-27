class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        '''
        # build 6 sets
        #check all num from 1-6 if appear in all sets (max would be 2 numbers)
        # for these common nums, check top and bottom to check the count and return the min
        
        
        # build 6 sets
        sets = []
        for i in range(len(tops)):
            sets.append(set([tops[i],bottoms[i]]))        
        
        #check all num from 1-6 if appear in all sets (max would be 2 numbers)
        common_numbers = []
        for i in range(1,7):
            inSet = True
            for s in sets:
                if i not in s:
                    inSet = False
                    break
            if inSet:
                common_numbers.append(i)
                if len(common_numbers)==2:
                    break
                    
        # for these common nums, check top and bottom to check the count and return the min
        if len(common_numbers)==0:
            return -1
        ans = float('inf')
        for x in common_numbers:
            count1,count2 = 0,0
            for n in tops:
                if n!=x:
                    count1 +=1
            for n in bottoms:
                if n!=x:
                    count2 +=1
            ans = min(ans, count1, count2)
            
        return ans
        '''
        
        #it should either be tops[0] or bottoms[0] if not found then no sol
        for target in [tops[0], bottoms[0]]:
            missingT = missingB = 0
            for i in range(len(tops)):
                top = tops[i]
                bottom = bottoms[i]
                if not (top == target or bottom == target):
                    break
                if top != target:
                    missingT += 1
                if bottom != target:
                    missingB += 1
                    
                if i==len(tops)-1:
                    return min(missingT, missingB)
        return -1
        