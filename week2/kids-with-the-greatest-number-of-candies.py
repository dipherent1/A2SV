class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False]*len(candies)
        maximum = max(candies)
        for i in range(len(candies)):
            result[i] = candies[i]+extraCandies>=maximum
        return result

        