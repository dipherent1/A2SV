class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix_prod = [1]*(len(nums)+1)
        postfix_prod= [1]*(len(nums)+1)
        for i in range(1,len(prefix_prod)):
            prefix_prod[i] = prefix_prod[i-1]*nums[i-1]
        print(prefix_prod)
        for i in range(len(postfix_prod)-1,0,-1):
            print(i-1)
            postfix_prod[i-1] = postfix_prod[i]*nums[i-1]
        print(postfix_prod) 
        for i in range(len(nums)):
            result.append(prefix_prod[i]*postfix_prod[i+1])
        return (result)