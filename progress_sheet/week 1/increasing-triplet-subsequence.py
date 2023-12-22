class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        mn = float("inf")
        count = 0
        a = float("-inf")
        for i in nums:
            if i > mn:
                count +=1
                a = mn
                mn = i
            if i > a:
                mn = min(mn,i)
            if i < a:
                a = i
            if count == 2:
                return True

        