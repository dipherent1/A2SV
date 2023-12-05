class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        for ghost in ghosts:
            xdistance = ghost[0]-target[0]
            ydistance = ghost[1]-target[1]
            if abs(target[0])+abs(target[1])>=abs(xdistance)+abs(ydistance):
                return False

        return True