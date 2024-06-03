class Solution:
    def clearStars(self, s: str) -> str:
        # using heap to store the smallest character, and also the rightmost instance of it
        tracker = [False for _ in range(len(s))]
        print(tracker)

        heap = []
        for index, char in enumerate(s):
            if char == '*':
                least_char, pos = heapq.heappop(heap)
                tracker[index] = True
                tracker[-pos] = True
            else:
                # Push tuple (char, -index) to invert the priority of the index
                heapq.heappush(heap, (char, -index))

        res = ""

        for index, char in enumerate(s):
            if not tracker[index]:
                res += char
        return res