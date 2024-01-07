class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        #intersections is above the max start and below min end
        # | |--->     <-----|   |
        #only intersects if max of start is behind and the min end
        i,j = 0,0
        ans = []
        while i<len(firstList) and j<len(secondList):
            l = max(firstList[i][0], secondList[j][0])
            r = min(firstList[i][1], secondList[j][1])

            if l<=r:
                ans.append([l,r])
                if secondList[j][1]>firstList[i][1]:
                    i+=1
                else:
                    j+=1
            else:
                if secondList[j][1]>firstList[i][1]:
                    i+=1
                else:
                    j+=1
        return ans
