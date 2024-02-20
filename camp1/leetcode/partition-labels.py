class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        visited = set()
        l = 0
        ans = []
        for r in range(len(s)):
            visited.add(s[r])
            count[s[r]]-=1
            
            if count[s[r]] == 0:
                visited.remove(s[r])
            
            if len(visited) == 0:
                ans.append(r-l+1)
                l = r+1
        return ans