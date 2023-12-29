class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        for i in range(len(s)):
            s[i] = [s[i][-1],s[i][:-1]]
        s.sort()
        ans = []
        for ind,sentences in s:
            ans.append(sentences)
        return " ".join(ans)
        
        