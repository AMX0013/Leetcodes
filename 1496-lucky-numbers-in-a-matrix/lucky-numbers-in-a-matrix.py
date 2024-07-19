class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        res = []
        for row in matrix:
            candidate = min(row)
            j = row.index(candidate)
            # print(j)

            col = [matrix[i][j] for i in range(len(matrix))]

            if max(col) == candidate:
                res.append(candidate)
        return res
        