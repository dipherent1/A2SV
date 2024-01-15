class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        count1 = Counter(s2[:len(s1)-1])
        l = 0
        for r in range(len(s1)-1,len(s2)):
            count1[s2[r]]+=1
            if count1 == count:
                return True
            count1[s2[l]] -= 1
            if not count1[s2[l]]:
                del count1[s2[l]]
            l+=1