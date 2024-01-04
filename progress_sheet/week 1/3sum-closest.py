class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        sums = set()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l<r:
                sums.add(nums[i]+nums[l]+nums[r]) 
                if nums[i]+nums[l]+nums[r]>target:
                    r-=1
                elif nums[i]+nums[l]+nums[r]<target:
                    l+=1
                else:
                    return nums[i]+nums[l]+nums[r]
        print(sums)
        diff = float("inf")
        ans = 0
        for i in sums:
            if abs(i-target)<diff:
                diff = abs(i-target)
                ans = i
        return ans
