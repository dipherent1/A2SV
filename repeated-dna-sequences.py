class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, ans = set(),set()
        for i in range(len(s)-9):
            cur = s[i:i+10]
            if cur in seen:
                ans.add(cur)
            seen.add(cur)
        return list(ans)