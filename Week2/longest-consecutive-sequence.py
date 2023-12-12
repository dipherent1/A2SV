class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        ans = 0
        while set1:
            cur_count = 1
            num = set1.pop()
            store = num
            while num+1 in set1:
                num+=1
                set1.remove(num)
                cur_count +=1
            num = store
            while num-1 in set1:
                num-=1
                set1.remove(num)
                cur_count +=1
            ans = max(ans,cur_count)
        return ans