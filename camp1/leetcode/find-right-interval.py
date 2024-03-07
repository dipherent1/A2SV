class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        temp = [inter[0] for inter in intervals]
        temp.sort()

        check = {intervals[i][0]:i for i in range(len(intervals))}
        
        ans = []
        for start,end in intervals:
            val = bisect_left(temp,end)
            
            if val==len(intervals):
                ans.append(-1)
            else:
                ans.append(check[temp[val]])
        return ans

            