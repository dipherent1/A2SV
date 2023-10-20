class Solution:
    def firstUniqChar(self, s: str) -> int:
        q = defaultdict(int)
        for ch in s:
            q[ch]+=1
        for ch in s:
            if q[ch] == 1:
                return s.index(ch)
        return -1