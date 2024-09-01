class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res = []
        lenth = len(original)
        j=0
        if m*n != lenth:
            return res

        for col in range(m):

            res.append(original[j : j+n ])
            # print(res)
            j+=n
        return res