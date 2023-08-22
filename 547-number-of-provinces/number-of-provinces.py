# class unionFind:
#     def __init__(self,n):
#         # from Sir Abdul bari's video
#         # if the value at index i is 
#             # +ve : it indicates that there exists a parent node 
#             # -ve : value indicates that this index is a parent and 
#                     # the value is the rank of that node(no. of connected children)
        
#         parent_ranks = [-1 for _ in range(n)]


#     def find(self,node):
        
#         while  node >= 0  : # node != self.parent_ranks[node] and

#             # update the parent node by searching deeper
#             self.parent_ranks[node] = self.parent_ranks[self.parent_ranks[node]]
#             # update node to be queried as the immediate parent
#             node = self.parent_ranks[node]


#         return node

class unionFind:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
        self.rank = [1]*n
    
    def find(self,node):

        while node != self.parents[node]:
            self.parents[node] = self.parents[self.parents[node]]
            node = self.parents[node] 
        return node
    
    def union(self,v1,v2):
        p1 , p2 = self.find(v1) , self.find(v2) 
        if p1 == p2:
            # Both are root nodes, part of same connected entitiy
            return 0
        
        if self.rank[p2] > self.rank[p1] :
            self.rank[p2] += self.rank[p1]
            self.parents[p1] = p2
        else:
            self.rank[p1] += self.rank[p2]
            self.parents[p2] = p1
        return 1

class Solution:
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        cities = len(isConnected)

        uf = unionFind(cities)

        res = len(isConnected)

        for c1 in range(cities):

            for c2 in range(cities):

                if c1 == c2:
                    continue

                if isConnected[c1][c2] == 1:
                    res -= uf.union(c1,c2)
                    isConnected[c1][c2] =0
                    isConnected[c2][c1] =0
        return res
                
