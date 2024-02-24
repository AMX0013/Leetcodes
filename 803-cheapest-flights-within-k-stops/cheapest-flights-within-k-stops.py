class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj={i:[] for i in range(n+1)}
        for u,v,val in flights:
            adj[u].append((v,val))

        heapQ=[]
        
        # init
        price = 0
        hops  = 0
        
        visited = [10**9]*n
        # path = [src]
        # print(path)
        heapq.heappush(heapQ,(price,hops,src))
        
        resPrice = -1

        while heapQ:

            price, hops,curr = heapq.heappop(heapQ)
            
            print("price, hops,curr",price, hops,curr)

            if curr == dst:
                print("cheapest is ",price)
                resPrice = price
                break

            if hops>k:
                print("hopped a lot",hops,k,hops>k)
                continue
            # visited tracks if i have come to a node with said hops
            # if i come there again with more hops, its a longer path and can be pruned
            if hops >= visited[curr]  :
                print("visited ex again. Ex is :",curr)
                print(visited)
                continue
            visited[curr] = hops

            for next_dest, next_price in adj[curr]:
                # temp = path.copy()
                # temp.append(next_dest)
                heapq.heappush(heapQ,(price + next_price ,hops +1 ,next_dest ))
        
        return resPrice


