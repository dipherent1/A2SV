class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        idxs = {}
        ans = float("inf")
        for r in range(len(cards)):
            if cards[r] in idxs:
                ans = min(ans,r-idxs[cards[r]]+1)
            idxs[cards[r]] = r
        return -1 if ans == float("inf") else ans