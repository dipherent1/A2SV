class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_count = blocks[:k].count("W")
        l = 0
        temp_count = white_count
        # if blocks[0] == "W":
        #     temp_count = white_count-1
        # else: 
        #     temp_count = white_count

        for r in range(k,len(blocks)):
            if blocks[r] == "W":
                temp_count+=1
            if blocks[l] == "W":
                temp_count-=1
            # print(temp_count)
            white_count = min(white_count,temp_count)
            l+=1
        
        
        
        return white_count
        