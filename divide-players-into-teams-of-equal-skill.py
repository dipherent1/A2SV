class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill)-1
        product = 0
        skill_sum = 0
        while l < r:
            if skill_sum == 0:
                skill_sum+=(skill[l]+skill[r])
            if skill[l]+skill[r]!=skill_sum:
                return -1
            
            product += skill[l]*skill[r]
            l+=1
            r-=1
        return product