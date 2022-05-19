import heapq

class Solution:
    
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # walls are at x=0 and x = len(heightMap)-1 & y = 0 and y = len(heightMap[0)-1
        water = 0
        xAxis = len(heightMap)
        yAxis = len(heightMap[0])
        
        if xAxis  <3 or yAxis < 3:
            return water
        
        heap = []
        visited = [ [0 for b in range(yAxis) ] for a in range(xAxis) ]
        
        for i in range(xAxis):            
            for  j in range(yAxis):
                if i in {0,xAxis-1} or j in {0,yAxis-1}:
                    heapq.heappush(heap,[heightMap[i][j]  , i,j ])
                    visited[i][j] = heightMap[i][j]
            #print(visited[i])
                    
        
        
        directions = [ [1,0] , [-1,0] , [0,1] , [0,-1] ]
        
        while heap:
            height , i , j = heapq.heappop(heap)
            #print("popped height =",height)
            
            for direction in directions:
                
                newI = i + direction[0]
                newJ = j + direction[1]
                
                if 0<= newI < xAxis and  0<= newJ < yAxis  and visited[newI][newJ] ==0 :
                    #print(newI,newJ,">", heightMap[newI][newJ] )
                    visited[newI][newJ] = 1
                    if heightMap[newI][newJ] <= height:
                        
                        water+= height - heightMap[newI][newJ]
                        #print("popped water =",water)
                        heightMap[newI][newJ] = height                        
                    heapq.heappush(heap, [heightMap[newI][newJ] ,newI,newJ])
                    
        return water
            
        
        
                
                
                            