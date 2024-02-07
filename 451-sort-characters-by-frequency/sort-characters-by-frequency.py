class Solution:
    def frequencySort(self, s: str) -> str:
        res = []
        for char in set(s):
            freq = s.count(char)
            res.append((-freq,char))

        heapq.heapify(res)
        retStr = ""
        while res:
            freq,char = heapq.heappop(res)
            retStr += "".join(char*-freq)
            print(retStr)

        return retStr