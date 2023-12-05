class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        freq,val = 0,0
        while 2*i+1<len(nums):
            freq, val = nums[2*i], nums[2*i+1]
            # if val>=len(nums):
            #     break
            ans+=[val]*freq
            i+=1
        return ans
        