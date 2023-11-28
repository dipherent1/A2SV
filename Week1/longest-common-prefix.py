class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        if len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            for words in strs[1:]:
                if i == len(words) or words[:i+1]!=strs[0][:i+1]:
                    return ans
            ans+=strs[0][i]
        return strs[0]