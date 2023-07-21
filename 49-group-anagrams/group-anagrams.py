class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramsDict = defaultdict(list)

        for stringy in strs:

            root = "".join(sorted(stringy))

            anagramsDict[root] = anagramsDict.get(root,[])
            anagramsDict[root].append(stringy)
        

        res = list(anagramsDict.values())
        print(res)
        return res
        

        