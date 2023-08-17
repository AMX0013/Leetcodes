class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        height = len(mat)
        width = len(mat[0])

        bfsQ = collections.deque()

        for h in range(height):
            for w in range(width):
                if mat[h][w]==0:
                    bfsQ.append((0,h,w))

        res = [[math.inf for _ in range(width)] for _ in range(height)]

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = [[False for _ in range(width)] for _ in range(height)]

        while bfsQ:
            # popleft from Queue
            dist,h,w = bfsQ.popleft()

            # populate distance 
            res[h][w] = min(res[h][w],dist)
            visited[h][w] = True

            for dir_h,dir_w in directions:

                dh = h+dir_h
                dw = w+dir_w

                if 0<=dh<height and 0<=dw<width and visited[dh][dw] == False:
                    bfsQ.append((dist+1,dh,dw))

        return res