class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        height = len(mat)
        width = len(mat[0])

        bfsQ = collections.deque()
        INF = 10**10

        res = [[INF for _ in range(width)] for _ in range(height)]

        for h in range(height):
            for w in range(width):
                if mat[h][w]==0:
                    res[h][w] = 0
                    bfsQ.append((h,w))


        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        # visited = [[False for _ in range(width)] for _ in range(height)]

        while bfsQ:
            # popleft from Queue
            h,w = bfsQ.popleft()

            
            # visited[h][w] = True

            for dir_h,dir_w in directions:

                dh = h+dir_h
                dw = w+dir_w

                # if 0<=dh<height and 0<=dw<width and visited[dh][dw] == False:
                if 0<=dh<height and 0<=dw<width and res[dh][dw] == INF:

                    # populate distance 
                    res[dh][dw] = res[h][w]+1
                    bfsQ.append((dh,dw))

        return res