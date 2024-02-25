class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minis = []
        temp = float("inf")
        stack = []

        for num in nums:
            minis.append(temp)
            temp = min(temp,num)
        
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1] < nums[i]:
                ind = stack.pop()
                if minis[i] < ind:
                    return True
            stack.append(nums[i])



