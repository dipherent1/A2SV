class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count1 = Counter(t)
        count2 = defaultdict(int)
        size = 0

        l = 0
        ans = [0,float('inf')]

        for r in range(len(s)):

            if s[r] in count1:
                count2[s[r]]+=1
            if count2[s[r]] == count1[s[r]]:
                size+=count1[s[r]]
            while size == len(t):
                if ans[1] - ans[0]  >= r-l+1:
                    ans = [l,r]
                count2[s[l]]-=1
                if count2[s[l]] < count1[s[l]]:
                    size-=count1[s[l]]
                l+=1

        if ans[1] == float('inf'):
            return ""
        return s[ans[0]:ans[1] + 1]