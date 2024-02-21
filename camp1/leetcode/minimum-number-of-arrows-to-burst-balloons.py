class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        last = points[0][1]
        count = 1
        first = 0

        print(points)

        for x1,x2 in points:
            first = max(first,x1)
            
            if x1>last:
                count+=1
                print(x1,x2,count)
                last = x2
            last = min(last,x2)
        
        return count

