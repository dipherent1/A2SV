class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        l = 0
        i = 0 
        r = len(nums)-1
        while l<r-1:
            i=l+1
            r = len(nums)-1
            while i < r:
                if -(nums[l]+nums[i]) > nums[r]:
                    i+=1
                elif -(nums[l]+nums[i]) < nums[r]:
                    r-=1
                elif nums[l]+nums[i] == -nums[r]:
                    ans.append([nums[l],nums[i],nums[r]])
                    while (nums[r] == nums[r-1]) and i<r:
                        r-=1
                        ans.append([nums[l],nums[i],nums[r]])
                        # r-=1
                    i+=1
                # i+=1
            l+=1
        
        B = []
        for i in ans:
            if i not in B:
                B.append(i)
        return B