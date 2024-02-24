class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:


        adj={i:[] for i in range(n+1)}
        for u,v,val in flights:
            adj[u].append((v,val))

        heapQ=[]
        
        # init
        price = 0
        hops  = 0
        
        visited = set()
        path = [src]
        print(path)
        heapq.heappush(heapQ,(price,hops,src))
        
        resPrice = 10**9

        while heapQ:

            price, hops,curr = heapq.heappop(heapQ)
            
            # print("price, hops,curr",price, hops,curr,path)

            # minheap-> cheapest will be found first
            if curr == dst:
                print("cheapest is ",price)
                return price

            if (str(price)+str(curr)) in visited:
                print("visited ex again. Ex is :",curr)
                continue

            
            if hops>k:
                # print("hopped a lot",hops,k,hops>k)

                continue

            for next_dest, next_price in adj[curr]:
                # temp = path.copy()
                # temp.append(next_dest)
                # heapq.heappush(heapQ,(price + next_price ,hops +1 ,next_dest,temp ))
                heapq.heappush(heapQ,(price + next_price ,hops +1 ,next_dest))


            visited.add(str(price)+str(curr))
        return -1


