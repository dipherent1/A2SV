class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index = {val:ind for ind,val in enumerate(nums)}
        ans = [0]*len(nums)
        for x,y in operations:
            index[y] = index[x]
            del index[x]
        for val,ind in index.items():
            ans[ind] = val
        return ans