class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)//3
        piles.sort(reverse = True)
        ans = 0
        for i in range(1,len(piles)-n,2):
            print(i)
            j = i%len(piles)
            ans+=piles[j]
        return ans