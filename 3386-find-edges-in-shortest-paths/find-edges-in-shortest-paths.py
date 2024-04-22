import heapq
from typing import List

class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        # result
        res = [False]*len(edges)
        # init bfsHeap to dist=0, src = 0, path
        bfsHeap = [(0,0,[])]
        # min_dist_to_node 
        minDist = [10**9 ] * n
        minDist[0] = 0
        # adjList
        adj = [[] for _ in range(n)]
        # create an adj list with the edge's index to be used in res
        for idx, (src,dest,wt) in enumerate(edges):
            adj[src].append((wt,dest,idx))
            adj[dest].append((wt,src,idx))
        

        while bfsHeap:

            dist, src, path = heapq.heappop(bfsHeap)
            

            if src == n-1 and dist <= minDist[src]:
                # reached
                for idx in path:
                    res[idx] = True

            for wt, dest, edgeId in adj[src]:
                
                newDist = dist + wt
                if newDist <= minDist[dest]:
                    minDist[dest] = newDist
                    newPath = list(path)
                    newPath.append(edgeId)
                    heapq.heappush(bfsHeap, (newDist, dest, newPath))
            
            
        print(minDist)
        return res
            

        # create a minheap to implement dijkstra's alg, with first element being distance
            # since we want the edge choice, we send the path as well in the minheap
            # and visited here will a int array ensure that the min dist for that node is captured

