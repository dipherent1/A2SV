class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        mx = float("-inf")
        points.sort()
        for i in range(1,len(points)):
            mx = max(mx,points[i][0]-points[i-1][0])
        return mx