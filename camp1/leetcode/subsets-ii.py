class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()

        def helper(i,path):
            
            ans.add(tuple(path[:]))
            
            if i == len(nums):
                return 
            
            for j in range(i,len(nums)):
                
                
                path.append(nums[j])
                helper(j+1,path)
                path.pop()
       
        helper(0,[])
        return ans