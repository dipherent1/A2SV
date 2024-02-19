class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = len(set(nums))
        visited = {}
        l = 0
        ans = 0
        count = 0 

        for r in range(len(nums)):
            visited[nums[r]] = 1+visited.get(nums[r],0)  
            while len(visited) == k and l<=r:
                
                count+=1
                if visited[nums[l]]>1:
                    visited[nums[l]] -=1
                else:
                   del visited[nums[l]]
                
                l+=1
            ans+=count
            
        return ans