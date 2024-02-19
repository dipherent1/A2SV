class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        ans = 0
        odd = 0

        for key,val in count.items():
            if val%2 == 0:
                ans+=val
            else:
                temp = odd
                odd = max(odd, val)
                if temp and odd == val:
                    ans+=temp-1
                elif temp:
                    ans+=val-1

        ans+=odd

        return ans