class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        dic = {}
        
        paragraph = ''.join([c if c.isalnum() else ' ' for c in paragraph])
        
        for w in paragraph.split():
            word = w.lower()
            
            if word not in banned:
                dic[word] = dic.get(word,0)+1
        
        return max(dic.items(),key=lambda x:x[1])[0]