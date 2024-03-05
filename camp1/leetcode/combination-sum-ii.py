class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []

        def helper(i,path):
            if sum(path) == target:
                ans.append(path[:])
                return 
            
            if sum(path) > target:
                return
            
            for j in range(i,len(candidates)):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                
                path.append(candidates[j])

                helper(j+1,path)

                path.pop()
        
        helper(0,[])
        return ans
