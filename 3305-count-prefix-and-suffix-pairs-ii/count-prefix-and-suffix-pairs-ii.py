class TrieNode():
    def __init__(self):
        self.kids = {}
        # self.is_word = false
        # additional utility vars for the problem
        self.matches = 0

class Trie():
    def __init__(self):
        # creates Trienode for root
        self.root = TrieNode()
    
    def createAndComputePS(self, word:str):
        # creates TrieNode
        # computes matches so far
        curr = self.root
        prev_matches = 0
        N = len(word)

        for i in range(N):
            # idx/key is tuple of first and last char of the word combined, to ensure 2way traversal
            idx = (word[i] , word[N-1-i] )
            if idx not in curr.kids:
                # create new node
                curr.kids[idx] = TrieNode()
            curr = curr.kids[idx]
            prev_matches += curr.matches
        # A word is always a prefix and suffix of itself
        curr.matches+=1
        # but does not abide i < j, thus we return only its prev matches
        return prev_matches

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # soln: search words and words.reverse. The result of number of is_words for the word is what we need
        # recursive calls to search?????
        trie = Trie()
        res = 0
        for word in words:
            res += trie.createAndComputePS(word)
        return res

        
        