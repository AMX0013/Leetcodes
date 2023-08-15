class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dfsStack = []


        direction = [(1,0) , (0,1) ]
        # 1 array is enough
        memo = [0 for _ in range(n)] 
        # # inititalise the memo for the dest
        memo[-1] = 1
  
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0]:
            return 0


        # DP : Since valid moves are bottom and right, we go top and leftwards
            #   Accessing only bottom and right values
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if obstacleGrid[i][j]==1:
                    memo[j] = 0
                else:
                    if j < n-1:
                        memo[j] = memo[j]+memo[j+1]
                
            
        return memo[0]






        # memo = [[0 for _ in range(n)] for _ in range(m)]   

        # # inititalise the memo for the dest
        # memo[m-1][n-1]=1


        # def recurDFS(i,j):
            
        #     if obstacleGrid[i][j]==1:
        #         return 0

        #     if memo[i][j] !=0:
        #         return memo[i][j]

        #     for x,y in direction:
        #         # print(x,y)
        #         dx = i+x
        #         dy = j+y
                

        #         if 0<=dx<m and 0<=dy<n  :
        #             # print(">",dx,dy)
        #            memo[i][j] += recurDFS(dx,dy)

        #     return memo[i][j]

        # recurDFS(0,0)
        # for i in range(m):
        #     print(memo[i])
        # return memo[0][0]