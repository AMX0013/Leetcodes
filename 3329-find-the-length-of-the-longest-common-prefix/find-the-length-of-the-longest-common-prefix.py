class Trienode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie:

    def __init__(self):
        # always start from here
        self.root = Trienode()

    def insert(self, word: str):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = Trienode()
            # traverse
            node = node.children[char]
        node.is_end = True

    def search(self, word:str):
        node = self.root
        prefix = 0
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            prefix +=1            

        return prefix



class Solution:

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        die_trie = Trie()
        for word in arr1:
            die_trie.insert(str(word))
        res = 0
        for word in arr2:
            curr_pre = die_trie.search(str(word))
            # print(word, curr_pre)
            res = max(res, curr_pre)

        return res
        
        