class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0]-x[1])
        ans = 0
        for i in range(len(costs)//2):
            ans+=costs[i][0]
            
        for i in range(len(costs)//2):
            j = (len(costs)//2)+i
            ans+=costs[j][1]
            
        return ans