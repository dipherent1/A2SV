class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter(p)
        n = len(p)
        ans = []
        for i in range(len(s)-n+1):
            count2 = Counter(s[i:i+n])
            if count == count2:
                ans.append(i)
        return ans