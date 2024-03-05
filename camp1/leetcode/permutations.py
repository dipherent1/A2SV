class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        l = len(nums)
        visited = set()

        def helper(i,path):

            if len(path) == l:
                ans.append(path[:])
                return 
            
            for j in range(0,l):
                
                if nums[j] in visited:
                    continue
                
                path.append(nums[j])
                visited.add(nums[j])
                helper(j+1,path)
                
                path.pop()
                visited.remove(nums[j])
        
        helper(0,[])
        return ans


