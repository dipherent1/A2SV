class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans = []
        presum = [0,nums[0]]
        postsum = [0,nums[-1]]
        n = len(nums)

        for i in range(1,len(nums)):
            presum.append(presum[-1]+nums[i])
            postsum.append(postsum[-1]+nums[len(nums)-i-1])

        print(presum)
        print(postsum)

        for i in range(1,n+1):
            sufftemp = postsum[n-i]-(nums[i-1]*(n-i))
            pretemp = (nums[i-1]*(i))-presum[i]
            ans.append(sufftemp+pretemp)
        
        return ans