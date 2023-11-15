class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        '''
        "aba defde hijhij"
         
        "eccbbbbdec"

        # 2a  3
        # 1b
        
        # 2d
        # 2e
        # 1f 5

        # 2h
        # 2i
        # 2j 6
        
        2a
        1b
        
        2d
        2e
        1f
        
        2h
        2i
        2j

        '''
        count = Counter(s)
        sub_count = defaultdict(int)
        ans = []
        # is_partition = True
        
        for char in s:
            sub_count[char] = 1+sub_count.get(char,0)
            is_partition = True
            for key, value in sub_count.items():
                if count[key]!=value:
                    is_partition = False
                    break
            if is_partition:
                ans.append(sum(sub_count.values()))
                sub_count = defaultdict(int)
                # is_partition = True
        return ans