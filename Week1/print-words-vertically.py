class Solution:
    def printVertically(self, s: str) -> List[str]:
        lst = s.split()
        m = 0
        for i in lst:
            m = max(m,len(i))
        ans = [""]*m
        for l in range(m):
            for words in lst:
                if l<len(words):
                    ans[l]+=words[l]
                else:
                    ans[l]+=" "
        ans = [word.rstrip() for word in ans]
        return ans