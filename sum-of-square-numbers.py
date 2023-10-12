class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        r = int(sqrt(c))
        l = 0
        while l<=r:
            powl = l*l
            powr = r*r
            if powl + powr == c:
                return True
            elif powl + powr < c:
                l+=1
            else:
                r-=1
        return False