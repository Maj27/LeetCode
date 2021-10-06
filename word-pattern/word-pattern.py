class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        dic ={}
        if len(words)!=len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in dic:
                if dic[pattern[i]]!=words[i]:
                    return False
            elif words[i] in dic.values():
                return False
            else:
                dic[pattern[i]]= words[i]
       
        return True
 