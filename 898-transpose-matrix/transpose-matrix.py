class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        Y = len(matrix)
        X = len(matrix[0])
        res = [[0 for _ in range(Y)] for _ in range(X)]
        for i in range(Y):
            for j in range(X):
                res[j][i] = matrix[i][j]
        return res 

        