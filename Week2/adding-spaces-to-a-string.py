class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        start = 0
        for i in spaces:
            ans+=s[start:i]
            ans+=" "

            start = i
        return ans+s[start:]