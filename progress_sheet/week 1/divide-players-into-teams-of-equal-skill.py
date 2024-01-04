class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill)-1
        ans = 0
        summ = skill[l]+skill[r]
        while l<r:
            if skill[l]+skill[r] !=summ:
                return -1
            ans+=skill[l]*skill[r]
            l+=1
            r-=1
        return ans