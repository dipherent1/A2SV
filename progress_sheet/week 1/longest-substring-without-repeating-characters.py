class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = {s[0]}
        l = 0
        ans = 1
        for r in range(1,len(s)):
            while l<r and s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            ans = max(ans,r-l+1)
        return ans
        