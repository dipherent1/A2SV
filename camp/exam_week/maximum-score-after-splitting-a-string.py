class Solution:
    def maxScore(self, s: str) -> int:
        s = list(map(int, s))
        prefix = [0 for _ in range(len(s))]


        tot = 0
        for x in range(len(s)):
            tot+=s[x]
            prefix[x] = tot
        zeros = 0
        max_score = 0
        if not tot:
            return len(s)-1

        for x in range(len(prefix)-1):
            if s[x] == 0:
                zeros+=1
            max_score = max(max_score, prefix[-1] + zeros - prefix[x])

        return max_score