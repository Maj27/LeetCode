class WordDictionary:

    def __init__(self):
        self.word_dict = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.word_dict[len(word)].add(word)
    
    def match(self, candidate: str, word: str) -> bool:
        i = 0
        while i<len(word):
            if word[i]!=candidate[i] and word[i]!='.':
                return False
            i+=1
            
        return i==len(word)
           
        
    def search(self, word: str) -> bool:
        words = self.word_dict[len(word)]
        if not '.' in word:
            return word in words
        else:
            for w in words:	
                if self.match(w, word): 
                    return True
            return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)