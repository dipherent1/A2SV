class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)-1):
            point1 = points[i]
            point2 = points[i+1]
            diff1 = abs(point1[0] - point2[0])
            diff2 = abs(point1[1] - point2[1])
            if diff1 == diff2:
                ans += diff1
            else:
                if point1[0] == point2[0] or point1[1] == point2[1]:
                    ans += diff1 + diff2
                else:
                    temp = min(diff1, diff2)
                    ans += temp + abs(diff1 - diff2)
        return ans
