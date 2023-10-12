from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l = len(s)
        res = []
        i = 0
        last = {val: i for i, val in enumerate(s)}
        while i < l:
            end = last[s[i]]
            j = i
            while j < end:
                if last[s[j]] > end:
                    end = last[s[j]]
                j+=1
            res.append(end-i+1)
            i = end+1
        return res