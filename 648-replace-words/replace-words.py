class TrieNode():
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_word = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        curr = self.root

        for char in word:
            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                # create a new node for this char
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.is_word = True
        
    
    def search(self, word: str):
        curr = self.root
        wordLen = 0

        for char in word:

            if curr.is_word:
                return wordLen

            idx = ord(char) - ord('a')
            if not curr.children[idx]:
                #this word is not a part of our trie_dict
                return 0
            curr = curr.children[idx]
            wordLen +=1
        
    



class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        trie = Trie()

        for word in dictionary:
            trie.insert(word)

        # print(trie)

        sentence = sentence.split()
        N = len(sentence)

        for i in range(N):
            # print("searching : ", sentence[i])

            rootLen = trie.search(sentence[i])
            if rootLen !=0:
                word = sentence[i]
                sentence[i] = word[:rootLen]
        
        return " ".join(sentence)





        