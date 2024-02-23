class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse = True)
        print(deck)
        q = deque()
        for i in range(len(deck)):
            count = len(q)-1
            while count>0:
                q.append(q.popleft())
                count-=1
            q.appendleft(deck[i])
        return q
