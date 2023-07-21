class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sArr = [0] * 26
        pArr = [0] * 26

        res = []

        if len(p) > len(s):
            return res
        
        for char in p:
            pArr[ord(char) - ord('a')] +=1

        i = 0

        width = len(p)       

        ###### Initializiation ###############
        j = 0
        while j < len(p):
            sArr[ ord(s[j]) -ord('a')] +=1 
            j+=1

        if pArr == sArr:
            res.append(i)

        print(pArr )
        print()
        print(sArr)

        i+=1
        ######################################

        while i+width-1 < len(s):

            # good notion, in sliding window, its like an earthworm, u eat and poop

            sArr[ ord(s[i-1]) -ord('a')] -=1
            sArr[ ord(s[i+width-1]) -ord('a')] +=1


            if pArr == sArr:
                res.append(i)
            i+=1
        return res

