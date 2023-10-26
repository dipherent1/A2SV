class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        l = 0
        r = len(nums)-1

        while l<r-1:
            i=l+1
            r = len(nums)-1
            if l>0 and nums[l] == nums[l-1]:
                l+=1
                continue
            while i < r:
                if -(nums[l]+nums[i]) > nums[r]:
                    i+=1
                elif -(nums[l]+nums[i]) < nums[r]:
                    r-=1
                elif nums[l]+nums[i] == -nums[r]:
                    ans.append([nums[l],nums[i],nums[r]])
                    
                    i+=1
                    while nums[i]==nums[i-1] and i<r:
                        i+=1
                # i+=1
            l+=1
        

        return ans