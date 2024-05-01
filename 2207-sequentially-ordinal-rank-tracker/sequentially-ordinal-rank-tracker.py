class ComparitiveString:
# A String class with comparators
    def __init__(self,word):
        self.word = word
    
    def __lt__(self, other):
        return self.word > other.word
    
    def __eq__(self, other):
        return self.word == other.word

class SORTracker:

    def __init__(self):
        # create minHeap and maxHeap
        # minHeap to store the queried results
            # Note: do not sort by names for the same score. That is the reverse of how we need it.
            # cant negate lexicography for that
        self.queriedLocs = []
        # The maxHeap, stores the results yet to be queried
            # root containing the best location that hasnt been visited yed
        self.toBeExplored = []
        self.ith = 0

    def add(self, name: str, score: int) -> None:
        # implement  name as part as ComparitiveString class
        # Check if the newly added location is the best in rank or something, because, 
        # we'll have to push it to the visited list(the minHEap)
        name = ComparitiveString(name)
        # check top

        if len(self.queriedLocs)>0:

            curr_best_scor, curr_best_loc = self.queriedLocs[0]
            
            if curr_best_scor < score or (curr_best_scor == score and curr_best_loc.word > name.word):
                visited_scor, visited_loc = heapq.heappop(self.queriedLocs)
                # Push the OP loc into visited
                heapq.heappush(self.toBeExplored,(-visited_scor,visited_loc.word) )
                # push the popped one into to be explored
                heapq.heappush(self.queriedLocs,(score,name) )

            else:
                heapq.heappush(self.toBeExplored,(-score,name.word) )
        else:
            heapq.heappush(self.toBeExplored,(-score,name.word) )
        #print(self.toBeExplored)
        #print(self.queriedLocs)

    def get(self) -> str:
        
        neg_best_score, best_name = heapq.heappop(self.toBeExplored)
        self.ith += 1
        # push into visited/ queriedLocs, a minHeap
            # so that the least best loc can be visited again if a new highscore loc comes in
            # weird
        heapq.heappush(self.queriedLocs, (-neg_best_score, ComparitiveString(best_name) ) )
        #print("----------GET()--------------")
        #print("|",self.toBeExplored,"|")
        #print("|",self.queriedLocs,"|")
        #print("----------",best_name,"----------")
        #print()
        return best_name
        


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()