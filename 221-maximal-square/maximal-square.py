class Solution:
    
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        width = len(matrix)
        depth = len(matrix[0])
        maxSqr = 0
        # if width <1 or depth < 1:
            
        for i in range(width):
            for j in range(depth):  
                maxSqr = max(int(matrix[i][j]),maxSqr)
                if maxSqr ==1:
                    break
            
        
        # for i in range(2):
        #     for j in range(2):  
        #         maxSqr = max(int(matrix[i][j]),maxSqr)
        
        for i in range(1,width):
            
            for j in range(1,depth):
                curr = int(matrix[i][j])

                if curr != 0:
                    # initialized to 1 if 
                    maxSqr = max(maxSqr , curr)
                    
                    left = int(matrix[i][j-1])
                    up   = int(matrix[i-1][j])
                    diag = int(matrix[i-1][j-1])
                    # print("For i=",i,"j =",j)
                    # print("up =",up,"left =",left,"diag =",diag)
                    res = min(left,up,diag, ) 
                    # print("min =", res)
                    if res >0:
                        matrix[i][j] = int(res+1)
                    maxSqr = max(int(matrix[i][j])*int(matrix[i][j]),maxSqr)
            print(matrix[i])

        return maxSqr



