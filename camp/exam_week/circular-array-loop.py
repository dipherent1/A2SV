class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited = set()
        for i in range(len(nums)):
            seen = set()    
            while True:
                if i in seen:
                    return True
                if i in visited:
                    break
                seen.add(i)
                visited.add(i)
                prev = i
                i = (i+(nums[i]))%len(nums)
                if prev == i or (nums[i] > 0) != (nums[prev] > 0): 
                    break
