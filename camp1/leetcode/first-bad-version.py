# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, r: int) -> int:
        l = 1
        

        while l<=r:
            mid = (l+r)//2
            if isBadVersion(mid):
                r = mid-1
            else:
                l = mid+1
        print(l,r,mid)
        return l
        