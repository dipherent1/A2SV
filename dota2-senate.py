class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D, R = deque(),deque()
        for i,ch in enumerate(senate):
            if ch == "R":
                R.append(i)
            else:
                D.append(i)
        while D and R:
            d = D.popleft()
            r = R.popleft()
            if d < r:
                D.append(d+len(senate))
            else:
                R.append(r+len(senate))
        return "Dire" if D else "Radiant"