class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        ans = []
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                even_sum+=nums[i]

        for val,ind in queries:
            before = nums[ind]
            nums[ind]+=val
            after = nums[ind]
            if before%2 and  after%2 == 0:
                even_sum+=after
            elif before%2==0 and  after%2:
                even_sum-=before
            elif before%2==0 and  after%2 == 0:
                even_sum+=val

            # print(nums)
            ans.append(even_sum)

        return [0] if not ans else ans
            
        