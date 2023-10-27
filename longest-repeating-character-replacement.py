class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] not in hash_map:
                hash_map[s[r]] = 1
            else:
                hash_map[s[r]]+=1
            while (r-l+1) - max(hash_map.values())>k:
                hash_map[s[l]]-=1
                l+=1
            res = max(res,r-l+1)
        return res