import heapq
from typing import List

class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        res = [False] * len(edges)

        # Create adjacency list
        adj = [[] for _ in range(n)]
        for index, (ai, bi, wi) in enumerate(edges):
            adj[ai].append((wi, bi, index))
            adj[bi].append((wi, ai, index))

        # Priority queue for BFS, starting from node 0
        bfsHeap = [(0, 0, [])]  # (distance to node, node, edges used)
        min_dist = [float('inf')] * n  # Track the shortest distance to each node
        min_dist[0] = 0  # Distance to start node is 0

        while bfsHeap:
            # print(bfsHeap)
            dist, src, edgesUsed = heapq.heappop(bfsHeap)
            # print("popped node:", src)
            # If we reach the destination with a potential new shortest path
            if src == n - 1 and dist <= min_dist[n-1]:
                for idx in edgesUsed:
                    res[idx] = True

            # Explore each adjacent node
            for wt, dest, edgeId in adj[src]:
                new_dist = dist + wt
                if new_dist <= min_dist[dest]:
                    newPath = list(edgesUsed)
                    newPath.append(edgeId)
                    min_dist[dest] = new_dist

                    # print("adding to heap: ", dest)
                    heapq.heappush(bfsHeap, (new_dist, dest, newPath ))

        return res

