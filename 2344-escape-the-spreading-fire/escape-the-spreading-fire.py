class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:       
        
        # for row in range(len(grid)):
        #     print(grid[row])


        height = len(grid)
        width = len(grid[0])
        
        src =  (0,0)
        dest = (height-1,width-1)
        
        src_i , src_j = src
        dest_i, dest_j = dest

        # Game rigged from the start
        if grid[src_i][src_j] != 0 and grid[dest_i][dest_j] != 0:
            print("missfire?")
            return -1

        # BFSQ for fire
        fireQ = collections.deque()        

        fire_plane =  [[10**9 for _ in range(width)] for _ in range(height)]
        agent_plane = [[10**9 for _ in range(width)] for _ in range(height)]
        

        # bfsQ for our agent
        agentQ = collections.deque()
        agent_plane[src_i][src_j]=0
        agentQ.append(src)

        # populate initial matrices
        for h in range(height):
            for w in range(width):
                # multisourceBFS for fore
                if grid[h][w]==1:
                    fire_plane[h][w] = 0                    
                    fireQ.append((h,w))

        def bfs(queue , board , isAgent):
            directions = [(1,0),(0,1),(-1,0),(0,-1)]

            # BFS to obtain shortest path to destination
            while len(queue)>0:
                i,j = queue.popleft()

                for dir_i , dir_j in directions:

                    di = i + dir_i 
                    dj =  j + dir_j

                    if 0<=di<height and 0<=dj<width and board[di][dj] == 10**9 and grid[di][dj] != 2 :

                        board[di][dj] = board[i][j]+1                        
                        queue.append((di,dj))
                        
            # print("isAgent",isAgent)
            # for row in range(len(board)):
            #     print(board[row])
            # print("/////////////////////////////")

        # bfs for fire
        bfs(fireQ,fire_plane,False)
        # bfs for agent
        bfs(agentQ,agent_plane,True)

        

        fireTime = fire_plane[-1][-1]
        agentTime = agent_plane[-1][-1]

        # fire spreads faster than agent can reach 
        if fireTime < agentTime:
            return -1

        # fire cant reach
        if fireTime == 10**9 and fireTime > agentTime :
            return 10**9

        # agnet walled off and cant reach
        if agentTime == 10**9:
            return -1

        diff = fireTime - agentTime
        
        if diff <0:
            return -1
        # both reach safehouse from 2nd last row 
        downDiff = fire_plane[-2][-1] - agent_plane[-2][-1]

        # both reach safehouse from last row 
        rightDiff = fire_plane[-1][-2] - agent_plane[-1][-2]



        if downDiff > diff or rightDiff > diff:
            return diff

        return diff -1

        # return -1

