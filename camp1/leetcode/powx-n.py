class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        if n % 2 == 0:
            result = self.myPow(x, n // 2)
            return result * result
        else:
            result = self.myPow(x, (n - 1) // 2)
            return x * result * result
