class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = []
        valid_loosers = []
        players = set()
        losses = {}
        for winner,loser in matches:
            losses[loser] = losses.get(loser,0)+1
            players.add(winner)
            players.add(loser)
        for player in players:
            if player not in losses:
                winners.append(player)
            elif losses[player] == 1:
                valid_loosers.append(player)
        winners.sort()
        valid_loosers.sort()
        return [winners,valid_loosers]
