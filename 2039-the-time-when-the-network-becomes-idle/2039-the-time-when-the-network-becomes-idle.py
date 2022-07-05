class Solution:
    
    def bfsShortedDist(self, edgeDict, numNodes,patience):
        '''shortestPathLen = defaultdict(int)
        shortestPathLen[0] = 0'''
        
        #bfs yields shortest path from 0
        #insert neighbor and distance from 0 into Queue`
        
        dq = collections.deque([(0,0)])
        visited = [0 for i in range(numNodes)]
        timeList = [None for x in range(numNodes)]
        while dq:
            keyNodes,lenth = dq.pop()
            if visited[keyNodes] == 1:
                continue
            visited[keyNodes] = 1
            '''if shortestPathLen[node] :
                shortestPathLen[node] = min(lenth,shortestPathLen[node])
            else:
                shortestPathLen[node] = lenth'''
            roundTime = 2*lenth
            currPatience = patience[keyNodes]
            
            
            for nodes in edgeDict[keyNodes]:
                if visited[nodes] != 1:
                    dq.appendleft(( nodes,lenth+1 ))
                    
                    
            if keyNodes==0:
                timeList[keyNodes]=0
                #print("0:",timeList)
                continue
            #print("\ncurrPatience :",currPatience,"| Rountime",roundTime ," | keyNodes :",keyNodes)
            if currPatience < roundTime: # find mod, and at that sec a new msg will  spawn
                
                
                S = (roundTime -1) // currPatience
                
                #print("Spawns: ",S)
                
                lastSpawnTime = S*currPatience
                itsQuietTime = lastSpawnTime + roundTime+1
                timeList[keyNodes]=itsQuietTime
                
                #print("    timeList[",keyNodes,"] >",timeList[keyNodes],"|lastSpawnTime =>",lastSpawnTime , "| itsQuietTime =>",itsQuietTime  )
            
            else:
                timeList[keyNodes]=roundTime + 1    
                
                
            
        return  max(timeList)       
                
        
    
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        edgeDict = defaultdict(list)
        
        for pairs in edges:
            edgeDict[pairs[0]].append(pairs[1])
            edgeDict[pairs[1]].append(pairs[0])
        numNodes = len(patience)
        return self.bfsShortedDist(edgeDict, numNodes,patience)
        
        
        #print(shortestPathLen)
        
        '''
        for keyNodes in shortestPathLen:
            roundTime = 2*(shortestPathLen[keyNodes])
            currPatience = patience[keyNodes]
            if keyNodes==0:
                timeList[keyNodes]=0
                #print("0:",timeList)
                continue
            #print("currPatience :",currPatience,"| Rountime",roundTime ," | keyNodes :",keyNodes)
            if currPatience < roundTime: # find mod, and at that sec a new msg will  spawn
                
                
                S = (roundTime -1) // currPatience
                
                #print("Spawns: ",S)
                
                lastSpawnTime = S*currPatience
                itsQuietTime = lastSpawnTime + roundTime+1
                timeList[keyNodes]=itsQuietTime
                #print("timeList[",keyNodes,"] >",timeList[keyNodes],"|lastSpawnTime =>",lastSpawnTime , "| itsQuietTime =>",itsQuietTime  )
            
            else:
                timeList[keyNodes]=roundTime + 1
        
                print("satisfied timeList[",keyNodes,"] >",timeList[keyNodes])
        print("\n timeList : ",timeList)
        
        return max(timeList)'''
                
                
            
            