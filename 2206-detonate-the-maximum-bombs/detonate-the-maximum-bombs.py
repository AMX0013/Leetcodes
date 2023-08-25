
# class unionFind:

#     def __init__(self,n):
#         self.parent = [i for i in range(n) ]
#         self.rank = [1]*n

#         self.size = [1] * n

#     def maxExuplooosions(self):
#         return max(self.rank)

#     def find(self,bomb):

#         while bomb != self.parent[bomb]:

#             self.parent[bomb] = self.parent[self.parent[bomb]]

#             bomb =  self.parent[bomb]

#         return bomb

#     def union(self , bomb1 , bomb2):
#         # root1 = self.find(bomb1)
#         # root2 = self.find(bomb2)

#         # if root1 != root2:

#         #     if self.rank[root1] > self.rank[root2]:

#         #         self.rank[root1]+=self.rank[root2]
#         #         self.parent[root2] = root1
            
#         #     else:
                
#         #         self.rank[root2]+=self.rank[root1]
#         #         self.parent[root1] = root2

#         rootX = self.find(bomb1)
#         rootY = self.find(bomb2)

#         if rootX != rootY:
#             if self.rank[rootX] < self.rank[rootY]:
#                 rootX, rootY = rootY, rootX
#             self.parent[rootY] = rootX
#             if self.rank[rootX] == self.rank[rootY]:
#                 self.rank[rootX] += 1
#             self.size[rootX] += self.size[rootY]

    


class Solution:

    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        # uf = unionFind(len(bombs))

        # adjacency list containing directed edges

        adj = defaultdict(list)

        # amortised time: O(nxn)
        for bomb1 in range(len(bombs)):
            for bomb2 in range(bomb1+1,len(bombs)):
                x1,y1,rad1 = bombs[bomb1]
                x2,y2,rad2 = bombs[bomb2]

                dist = math.sqrt( (x2-x1)**2 + (y2-y1)**2 )

                if dist <= rad1:
                    # bomb1 can trigger bomb2
                    adj[bomb1].append(bomb2)
                    # uf.union(bomb1,bomb2)
                if dist <= rad2:
                    # bomb1 can trigger bomb1
                    adj[bomb2].append(bomb1)

                    # uf.union(bomb2,bomb1)


        def recurDFS(bombID , visSet):
            
            if bombID in visSet:
                return 0

            visSet.add(bombID)
            for bombs in adj[bombID]:
                recurDFS(bombs,visSet)

            return len(visSet)
        res = 0
        for bomb in range(len(bombs)):
            res = max(res,recurDFS(bomb,set() ))

        return res


