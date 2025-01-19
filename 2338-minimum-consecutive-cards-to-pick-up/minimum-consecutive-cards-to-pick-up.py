import heapq
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        cardsCounter =Counter(cards)
        l=0
        r=len(cards)-1
        if max(cardsCounter.values())<2:
            return -1
        cardsPos = defaultdict(list)
        shrtHand = []
        for idx,num in enumerate(cards):
            cardsPos[num].append(idx)
            if len(cardsPos[num])>=2:
                heapq.heappush(shrtHand,  cardsPos[num][-1] - cardsPos[num][-2]+1 )
        shortestDist = heapq.heappop(shrtHand)
        return shortestDist





        