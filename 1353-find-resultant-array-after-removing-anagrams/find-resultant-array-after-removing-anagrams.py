class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        
        res.append(words[0])

        for i in range(1,len(words)):
            root = "".join(sorted(words[i]))
            prevRoot = "".join(sorted(words[i-1]))
            if root == prevRoot:
                continue
            else:
                res.append(words[i])




        return res