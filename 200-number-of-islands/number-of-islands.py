class Solution:
        
    def numIslands(self, grid: List[List[str]]) -> int:
            
        width = len(grid[0])
        height = len(grid)
        count_islands = 0
        dir = [ (1,0), (0,1), (0,-1), (-1,0)]
        q = deque()

        y=0        
        while y < height:
            # print(visited)
            x=0
            while x < width:
                if  grid[y][x] =="1" :                      
                    node = (y,x)
                    count_islands += 1 
                    q.appendleft(node)
                    # bfs
                    while q:
                        curr_y, curr_x = q.pop()
                        if grid[curr_y][curr_x] == "0" :#already visited
                            continue
                        
                        grid[curr_y][curr_x] = "0"
                        for dir_y, dir_x in dir:
                            new_y = curr_y + dir_y
                            new_x = curr_x + dir_x

                            if new_y < height and \
                               new_x < width and \
                               new_y >= 0 and \
                               new_x >= 0 and \
                               grid[new_y][new_x] =="1":

                                node = (new_y,new_x)
                                q.appendleft(node)

                x+=1                
            y+=1
        
        return count_islands

    # def bfs(self,node, visited, grid, val, res):
    #     # print("bfs for ", node)
    #     if val =="1":
    #         res +=1
    #         # print("island exploring")
        
    #     dir = [ (1,0), (0,1), (-1,0), (0,-1)]
    #     q = deque()
    #     q.appendleft(node)
    #     width = len(grid[0])
    #     height = len(grid)
    #     next_search = node

    #     while q:
    #         curr_y, curr_x = q.pop()
    #         if (curr_y, curr_x) in visited:
    #             continue
    #         visited.add((curr_y, curr_x))

    #         for dir_y, dir_x in dir:
    #             new_y = curr_y + dir_y
    #             new_x = curr_x + dir_x
                
    #             if new_y < height and \
    #                new_x < width and \
    #                new_y >= 0 and \
    #                new_x >= 0 :
    #                 # print("hopeful", (new_y, new_x))  
    #                 if (new_y, new_x) in visited:  
    #                     # print("NOPE, visited", (new_y, new_x)) 
    #                     continue
    #                 else:
    #                     if grid[new_y][new_x] == val:    
    #                         # print("add", (new_y, new_x))           
    #                         q.appendleft( (new_y, new_x) )
    #                     else:
    #                         next_search = (new_y, new_x, grid[new_y][new_x])
    #                         new_y, new_x, val = next_search
    #                         res = self.bfs( (new_y, new_x), visited, grid, val, res )

    #     print(visited)
    #     return res

    # def numIslands(self, grid: List[List[str]]) -> int:
    #     visited = set()        
    #     width = len(grid[0])
    #     height = len(grid)
    #     count_islands = 0
              
       
        
    #     return self.bfs((0,0), visited, grid,grid[0][0] ,count_islands)
