class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        n = (num-3)//3
        if not (num-3)%3:
            return [n,n+1,n+2]
        return []
        