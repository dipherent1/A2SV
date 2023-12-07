class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        set_list = []
        left_covered = False
        right_covered = False
        r = set(range(left,right+1))
        for start, end in ranges:
            set_list.extend([i for i in range(start,end+1)])
        set_list = set(set_list)
        return r<=set_list