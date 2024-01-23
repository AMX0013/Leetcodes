

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        count = Counter(words)
        print(count)
        
        # creating heap
        heap = [(-freq,word) for word, freq in count.items()]
        heapify(heap)
        print(heap)

        return [heappop(heap)[1] for _ in range(k)]
        