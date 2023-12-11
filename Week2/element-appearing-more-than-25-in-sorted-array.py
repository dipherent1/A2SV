class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = Counter(arr)
        for key,val in count.items():
            if val>len(arr)/4:
                return key
        return 0

        