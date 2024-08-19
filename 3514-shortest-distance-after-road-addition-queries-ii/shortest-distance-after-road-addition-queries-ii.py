class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # index is node_id, val is node.next
        graph = [i+1 for i in range(n)]
        graph[-1] = -1
        print(graph)
        dist = n-1
        res = []
        for start, end in queries:
            if graph[start] != -1 and graph[start] < end:
                
                curr = start
                while curr != end:
                    
                    next_1 = graph[curr]
                    graph[curr] = -1
                    dist -=1
                    curr = next_1
                dist+=1
                graph[start]=end
                # print(graph)             
            
            res.append(dist)
            # print(res, start,end)
                
        return res

        