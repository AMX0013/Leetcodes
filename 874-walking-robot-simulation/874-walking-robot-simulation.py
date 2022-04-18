
from collections import defaultdict
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        count=0
        obstacleXdict = defaultdict(list)
        obstacleYdict = defaultdict(list)
        
        for x,y in obstacles:
            obstacleXdict[x].append(y)
            obstacleYdict[y].append(x)
        
        #print(obstacleXdict)
        for key , values in  obstacleXdict.items():
            values.sort()
        
            
        for key , values in  obstacleYdict.items():
            values.sort()
            
        #print(obstacleXdict)
        
        N = True
        E = False
        W = False
        S = False
        x = 0
        y = 0
        dist = []
        
        
            
        
        for command in commands:
            if command == -1:
                #change directions
                
                if N:
                    N = False
                    E = True
                elif E:
                    E = False
                    S = True
                    
                elif W:
                    W = False
                    N = True
                elif S:
                    S = False
                    W = True
            elif command == -2:
                #change directions
                
                if N:
                    N = False
                    W = True
                elif E:
                    E = False
                    N = True
                    
                elif W:
                    W = False
                    S = True
                elif S:
                    S = False
                    E = True
            else:
                # check obstacle  and move robot 
                length = command             
                
                
                
                
                if N: #obstacleYdict[x]
                    
                    yList = obstacleXdict[x]
                    y2 = y+length
                    
                    i  = bisect.bisect_right(yList, y)
                    if i < len(yList) and yList[i]<=y2:
                        y2 = yList[i]-1
                    y = y2
                    
                    print(count,"N>",x,y)
                
                elif E:
                    x2 = x+length
                    xList = obstacleYdict[y]
                    #print(xList)
                    i = bisect.bisect_right(xList, x)
                    if i < len(xList) and xList[i] <=x2:
                        x2 = xList[i]-1
                    x = x2
                    
                    print(count,"E>",x,y)
                    
                elif W:
                    x2 = x-length
                    xList = obstacleYdict[y]
                    i = bisect.bisect_left(xList, x)
                    if i  and xList[i-1] >=x2:
                        x2 = xList[i-1]+1
                    x = x2
                    print(count,"W>",x,y)
                elif S: #obstacleYdict[x]
                    
                    yList = obstacleXdict[x]
                    #print("y values >",yList)
                    y2 = y-length
                    
                    i  = bisect.bisect_left(yList, y)
                    
                    if i and yList[i-1]>= y2:
                        #print(i,yList[i-1])
                        y2 = yList[i-1]+1
                    y = y2
                    
                    print(count,"S>",x,y)
                    #abs
                dist.append(x*x+y*y) 
                count+=1
                #print("dist>",dist)
            #print((x*x+y*y) )
        
        return(max(dist))
        