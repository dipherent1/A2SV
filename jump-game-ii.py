class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        i iterates while its not the last
        while jumping we look for the next best place to  jump from  to jump the furthest max_jump and its index
        then we jump
        '''
        if len(nums) == 1:
            return 0
        i = 0
        jump = nums[0]
        count=0
        max_jump = 0
        while i < len(nums)-1:
            max_jump = 0
            furthest = i+nums[i]
            if furthest>=len(nums)-1:
                return count+1
            i+=1
            while i < len(nums) and i <= furthest:
                # furthest = i+nums[i]
                if i+nums[i] > max_jump:
                    j=i
                max_jump = max(i+nums[i],max_jump)
                i+=1
            i =j
            count+=1
        return count