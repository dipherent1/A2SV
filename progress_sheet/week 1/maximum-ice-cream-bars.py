class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        candy = 0
        tcost = 0
        for cost in costs:
            tcost+=cost
            if tcost>coins:
                return candy
            candy+=1
        return len(costs)