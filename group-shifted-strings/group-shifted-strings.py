class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        
        def hash_str(s):
            return tuple((ord(c)-ord(s[0]))%26 for c in s)
        
        dic = collections.defaultdict(list)
        for s in strings:
            dic[hash_str(s)].append(s)

        return dic.values()
        