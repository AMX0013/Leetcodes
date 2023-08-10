class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        # Instead of generating hamming distance for curr cell against all Thieves
        # We instead use a BFS style Queue operated population of the grid
        # with safety  levels

        # Action 1 : Generate safety level grid
        # Rule:
        # All the theif positions are 0
        # Initially insert these locations into a queue , along with this safety value
        # Pop from the queue each location
            # For all 4 directions that are valid:
                # Increase these 4 locations safety factor by 1
        # By end of this, you will have a saftey level map for the whole grid 

        def populateSafetyGrid():

            bfsQ = collections.deque()

            # Note : There might be a case where Theif positions will overlap and 
            # you populate a position that is 1 with value 2 , dont! . Enforce a check
            # of your choice
            safetyGrid = [[None for _ in range(len(grid))] for _ in range(len(grid[0]))]

            # Loading theif positions into Queue and populate safety grid
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==1:
                        bfsQ.append((0,i,j))
                        safetyGrid[i][j] = 0
            
            

            # Directions matrix for traversal in dirs!
            dirs = [(1,0),(0,1),(-1,0),(0,-1)]

            # Creating variable maxSafety for uuse in next operation
            maxSafety = 0
            # Pop from bfsQ and populate the safetyGrid
            
            while len(bfsQ) >0:
                safety,x,y = bfsQ.popleft()
                
                for dir_x , dir_y in dirs:
                    dx , dy = x + dir_x , y+dir_y
                    if 0 <= dx < len(grid) and 0<=dy<len(grid[0]) and safetyGrid[dx][dy] == None :
                        safetyGrid[dx][dy] = safety+1

                        maxSafety = max(maxSafety,safetyGrid[dx][dy])
                        # We mus save this value into queue for further population of the grid
                        bfsQ.append((safetyGrid[dx][dy],dx,dy))
                
            
            return safetyGrid , maxSafety
        
        safetyGrid ,maxSafety  = populateSafetyGrid()
        # print(safetyGrid)
        
        
        # Action 3:
        # Take chosen threshold, and enforce it on choosing those cells
        #  whose threshold value is greater than that . Use the same BFS logic as above

        def pathExistFor(safetyThreshold):
            dest = (len(grid)-1,len(grid[-1])-1)
            start = (0,0)
            
            # Check if start and dest positions even have safety level above safetyThreshold
            if safetyGrid[0][0] < safetyThreshold or safetyGrid[len(grid)-1][len(grid[-1])-1] < safetyThreshold :
                # print("Fails init chek")
                return False

            # Directions matrix for traversal in dirs!
            dirs = [(1,0),(0,1),(-1,0),(0,-1)]

            visited = [[False for _ in range(len(grid))] for _ in range(len(grid[0]))]

            dfsStack = []

            dfsStack.append(start)

            while len(dfsStack) >0:
                x,y = dfsStack.pop()
                visited[x][y] = True

                # print("(",x,",",y,")")
                if (x,y) == dest:
                    return True

                for dir_x , dir_y in dirs:
                    dx , dy = x + dir_x , y+dir_y

                    # print( "(",dx,",",dy,")" , "0 <= dx < len(grid)", 0 <= dx < len(grid) , " 0<=dy<len(grid[dx])",  0<=dy<len(grid[dx]) , "visited[dx][dy] == False",visited[dx][dy] == False)

                    if 0 <= dx < len(grid) and 0<=dy<len(grid[dx]) and visited[dx][dy] == False:
                        # print( "(",dx,",",dy,")" , safetyGrid[dx][dy] >= safetyThreshold  )
                        if safetyGrid[dx][dy] >= safetyThreshold:
                            dfsStack.append((dx,dy))
                # print(dfsStack , len(dfsStack))

            return False

        # Action 2
        # Use binary search to select minimum safety threshold that we can maintain 
        # and successfully make it to the Dest

        l = 0
        r = maxSafety
        res = 0

        # print("r = ",maxSafety)
        while l<=r:

            safetyThreshold = l + (r-l)//2
            # print(safetyThreshold)
            if pathExistFor(safetyThreshold):
                # print("# Increase Threshold search and try")
                res = safetyThreshold
                # Increase Threshold search and try
                l = safetyThreshold+1
            else:
                # print("# decrease threshold search")
                # decrease threshold search
                r = safetyThreshold-1



        return res