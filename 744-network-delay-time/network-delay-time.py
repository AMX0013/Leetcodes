class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # print(times)
        # implement dijkstra properly
        visited = set()
        adj_dict = defaultdict(tuple)
        for [src, dest, time] in times:
            

            adj_dict[src] = adj_dict.get(src,[])
            adj_dict[src].append((dest,time))


        print(adj_dict)
        print(visited)
        heapQ = []
        

        # distances, we are costructing the shortest path from each node.
        # thus all nodes are inf
        # then we go through immediate neighbours

        # dists = [float('inf') for _ in range(len(times))]
        # dist[k] = 0

        resTime = 0

        heapq.heappush(heapQ,(0,k))

        while heapQ:
            time, node = heapq.heappop(heapQ)
            if node in visited:
                continue
            visited.add(node)
            resTime = max(resTime, time)
            print("reached node",node,"whose min time iis", time, "at", resTime)
            for  neigh, n_time in adj_dict[node]:
                heapq.heappush(heapQ,(time+n_time,neigh))
        print(visited)
        if len(visited) ==n:
            return resTime
        return -1 
 