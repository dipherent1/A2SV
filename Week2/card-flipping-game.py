class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        ans = set()
        seen = set()

        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                seen.add(fronts[i])
                ans.discard(fronts[i])
                continue
            
            if fronts[i] in seen:
                ans.discard(fronts[i])
            else:
                ans.add(fronts[i])
            
            if backs[i] in seen:
                ans.discard(backs[i])
            else:
                ans.add(backs[i])
        
        return min(ans) if ans else 0

            
