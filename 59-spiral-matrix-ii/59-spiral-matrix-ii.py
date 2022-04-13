class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res= [[None for row in range(n)]for row in range(n)]
        top = 1
        bottom = n-1
        left = 0
        right = n-1
        num = 1
        i=0
        j=0
        LR = True
        UD = False
        RL = False
        DU = False
        while num <= n*n:
            if LR:
                if j == right:
                    LR = False
                    UD = True
                    right-=1
                    res[i][j] = num
                    num+=1
                    i+=1
                    
                    
                else:
                    res[i][j] = num
                    num+=1
                    j+=1
                    
                    
            elif UD:
                if i == bottom:
                    UD = False
                    RL = True
                    bottom-=1
                    res[i][j] = num
                    num+=1
                    j-=1
                    
                    
                else:
                    res[i][j] = num
                    num+=1
                    i+=1
                    
                    
            elif RL:
                if j == left:
                    RL = False
                    DU = True
                    left+=1
                    res[i][j] = num
                    num+=1
                    i-=1
                    
                    
                else:
                    res[i][j] = num
                    num+=1
                    j-=1
                    
            elif DU:
                #print(i,j)
                if i == top:
                    DU = False
                    LR = True
                    top+=1
                    res[i][j] = num
                    num+=1
                    j+=1
                    
                    
                else:
                                       
                    res[i][j] = num
                    num+=1
                    i-=1 
                    
            print(res)
            print("_____")
        return res
           
        