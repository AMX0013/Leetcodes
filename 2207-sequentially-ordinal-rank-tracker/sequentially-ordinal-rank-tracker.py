
class Location:
    def __init__(self, score, name):
        self.score = score
        self.name = name

    def __lt__(self, other):
        # Invert comparison to simulate max-heap behavior in a min-heap context
        return (self.score < other.score) or (self.score == other.score and self.name > other.name)

    def __eq__(self, other):
        return (self.score == other.score) and (self.name == other.name)

    def __repr__(self):
        return f"Location(score={self.score}, name='{self.name}')"

class SORTracker:
    def __init__(self):
        # minHeap to store elements already picked (in actual, normal order)
        self.minHeap = []
        # maxHeap to store elements to be picked next, handled by negative score for max behavior
        self.maxHeap = []

    def add(self, name: str, score: int) -> None:
        new_loc = Location(score, name)
        # Push the incoming element to the minHeap first
        heapq.heappush(self.minHeap, new_loc)
        # Move the top of the minHeap to the maxHeap
        new_loc = heapq.heappop(self.minHeap)
        heapq.heappush(self.maxHeap, (-new_loc.score, new_loc.name))
        # Remove the element moved to maxHeap from minHeap
        

    def get(self) -> str:
        # Retrieve the best location (next in line)
        neg_score, name = heapq.heappop(self.maxHeap)
        # Convert negative score back to positive
        real_score = -neg_score
        # Push it back to minHeap as it has now been processed
        heapq.heappush(self.minHeap, Location(real_score, name))
        return name

# class SORTracker:

#     def __init__(self):
#         # create minHeap and maxHeap
#         # minHeap to store the queried results
#             # Note: do not sort by names for the same score. That is the reverse of how we need it.
#             # cant negate lexicography for that
#         self.queriedLocs = []
#         # The maxHeap, stores the results yet to be queried
#             # root containing the best location that hasnt been visited yed
#         self.toBeExplored = []
#         self.ith = 0

#     def add(self, name: str, score: int) -> None:
#         # implement  name as part as ComparitiveString class
#         # Check if the newly added location is the best in rank or something, because, 
#         # we'll have to push it to the visited list(the minHEap)
#         name = ComparitiveString(name)
#         # check top

#         if len(self.queriedLocs)>0:

#             curr_best_scor, curr_best_loc = self.queriedLocs[0]
            
#             if curr_best_scor < score or (curr_best_scor == score and curr_best_loc.word > name.word):
#                 visited_scor, visited_loc = heapq.heappop(self.queriedLocs)
#                 # Push the OP loc into visited
#                 heapq.heappush(self.toBeExplored,(-visited_scor,visited_loc.word) )
#                 # push the popped one into to be explored
#                 heapq.heappush(self.queriedLocs,(score,name) )

#             else:
#                 heapq.heappush(self.toBeExplored,(-score,name.word) )
#         else:
#             heapq.heappush(self.toBeExplored,(-score,name.word) )
#         #print(self.toBeExplored)
#         #print(self.queriedLocs)

#     def get(self) -> str:
        
#         neg_best_score, best_name = heapq.heappop(self.toBeExplored)
#         self.ith += 1
#         # push into visited/ queriedLocs, a minHeap
#             # so that the least best loc can be visited again if a new highscore loc comes in
#             # weird
#         heapq.heappush(self.queriedLocs, (-neg_best_score, ComparitiveString(best_name) ) )
#         #print("----------GET()--------------")
#         #print("|",self.toBeExplored,"|")
#         #print("|",self.queriedLocs,"|")
#         #print("----------",best_name,"----------")
#         #print()
#         return best_name
        


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()