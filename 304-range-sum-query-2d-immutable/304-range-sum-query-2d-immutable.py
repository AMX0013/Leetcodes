class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSum2D = [[None for i in range(len(matrix[0]))] for i in range(len(matrix))]
        #for y in range(len(matrix)):
            #print(matrix[y])
        #print(self.prefixSum2D)
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                print(y,x)
                print(self.prefixSum2D[y][x])
                if y==0 and x==0:
                    self.prefixSum2D[y][x] = matrix[y][x]
                elif y==0 and x!=0:
                    self.prefixSum2D[y][x] = self.prefixSum2D[y][x-1] + matrix[y][x] 
                elif x ==0 and y!=0:
                    self.prefixSum2D[y][x] = self.prefixSum2D[y-1][x] + matrix[y][x]
                else:
                    self.prefixSum2D[y][x] = self.prefixSum2D[y-1][x] + self.prefixSum2D[y][x-1] + matrix[y][x] - self.prefixSum2D[y-1][x-1] # to prevent double addition of that value
                   
            #print(self.prefixSum2D[y])            
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 ==0:
            return self.prefixSum2D[row2][col2]
        elif row1 == 0:
            return ( self.prefixSum2D[row2][col2] - self.prefixSum2D[row2][col1-1] )
        elif col1 == 0:
            return ( self.prefixSum2D[row2][col2] - self.prefixSum2D[row1-1][col2] )
            
            
        else:
            return ( self.prefixSum2D[row2][col2] - ( self.prefixSum2D[row2][col1-1] + self.prefixSum2D[row1-1][col2]  -  self.prefixSum2D[row1-1][col1-1]  ) )
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)