class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) -1
        area = 0
        res = 0
        while i<=j:
            h = min(height[i],height[j])
            area = h * (j-i)
            res = max(area,res)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return res