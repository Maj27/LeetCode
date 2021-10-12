class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int

        """
    
        wordList = set(wordList)
        
        length = 1
        queue = deque([beginWord])
        while queue:
            
            new_q = deque()
            length+=1
            while queue:
                word = queue.popleft()
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i+1:]
                        if next_word == endWord and endWord in wordList:
                            return length
                        if next_word in wordList:
                            wordList.remove(next_word)
                            new_q.append(next_word)
            queue = new_q
            
        return 0