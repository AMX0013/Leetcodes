class Trienode:
    def __init__(self):
        self.is_word = False
        self.children = {}
        self.shrt_wrd_idx = None
        self.shrt_wrd_len = None
        # TODO: modify calculation to accomodate for it
           #holds len(wordsContainer[i] - len of longest common suffix with wordsQuery[self.idx] )

class Trie:
    def __init__(self):
        self.root = Trienode()
        # a common res that holds the index val of word from wordsContainer
        # self.res_values = []
        self.res = []

    def insert(self, word:str, idx )->None:
        curr = self.root
        word_len = len(word)

        for char in word:
            
            if curr.shrt_wrd_len == None or (curr.shrt_wrd_len != None and curr.shrt_wrd_len > word_len ):
                curr.shrt_wrd_len = word_len
                curr.shrt_wrd_idx = idx

            
            if char not in curr.children:
                curr.children[char] = Trienode()
            curr = curr.children[char]

        # print("at", curr.shrt_wrd_idx)
        curr.is_word = True
        if curr.shrt_wrd_len == None or (curr.shrt_wrd_len != None and curr.shrt_wrd_len > word_len ):
            curr.shrt_wrd_len = word_len
            curr.shrt_wrd_idx = idx
        
    def search(self, word: str, idx:int)->None:
        self.res.append(None)
        curr = self.root
        word_len = len(word)    
        for char in word:
            
            if char not in curr.children:
                # incase something unknow happens first
                self.res[idx] = curr.shrt_wrd_idx
                return
            # else, we continue the search
            curr = curr.children[char]
            self.res[idx] = curr.shrt_wrd_idx
            


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        
        suff_trie = Trie()
        # build the Trie for wordsContainer, a set of words
        for idx, word in enumerate(wordsContainer):
            word = word[::-1]
            # print("inserting",word)
            suff_trie.insert(word, idx)

        for idx, word in enumerate(wordsQuery):
            word = word[::-1]
            # print("searching the Longest suffix for", word)
            suff_trie.search(word, idx)
        
        return suff_trie.res
        