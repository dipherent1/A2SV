class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod = [1]
        running_prod = 1
        for num in nums:
            pre_prod.append(pre_prod[-1]*num)
        # print(pre_prod)
        for i in range(len(nums)-1,-1,-1):
            
            pre_prod[i]*=running_prod
            running_prod *= nums[i]
            # print(running_prod)

        return (pre_prod[:len(nums)])
        