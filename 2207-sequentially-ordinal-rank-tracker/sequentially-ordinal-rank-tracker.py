
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
