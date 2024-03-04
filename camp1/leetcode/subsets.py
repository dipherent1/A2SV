class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(i,path):
            
            ans.append(path[:])
            
            if i == len(nums):
                return 
            
            for j in range(i,len(nums)):
                
                path.append(nums[j])
                helper(j+1,path)
                path.pop()
       
        helper(0,[])
        return ans