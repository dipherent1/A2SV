class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        seen = defaultdict(int)
        l = 0
        ans = 0

        for r in range(len(fruits)):
            seen[fruits[r]]+=1
            while len(seen)>2:
                seen[fruits[l]]-=1
                if not seen[fruits[l]]:
                    del seen[fruits[l]]
                l+=1
            ans = max(ans,r-l+1)
        return ans
                