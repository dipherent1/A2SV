class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)
        l = 0
        ans = 0

        for r in range(len(s)):
            seen[s[r]]+=1
            while (r-l+1) - max(seen.values())>k:
                seen[s[l]]-=1
                if not seen[s[l]]:
                    del seen[s[l]]
                l+=1
            ans = max(ans,r-l+1)
        return ans