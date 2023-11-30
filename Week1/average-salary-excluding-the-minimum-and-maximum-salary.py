class Solution:
    def average(self, salary: List[int]) -> float:
        MaxSal = float("-inf")
        MinSal = float("inf")
        total = 0
        for val in salary:
            total+=val
            MaxSal = max(MaxSal,val)
            MinSal = min(MinSal,val)
        return (total-MaxSal-MinSal)/(len(salary)-2)