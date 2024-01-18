class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        freq = [0]*(len(nums)+1)
        for start, end in requests:
            freq[start]+=1
            freq[end+1]-=1
        for i in range(1,len(freq)):
            freq[i]+=freq[i-1]
        # print(freq)
        ans = 0
        freq.sort(reverse = True)
        nums.sort(reverse = True)
        for i in range(len(nums)):
            ans+=(freq[i]*nums[i])
        return ans%((10**9)+7)