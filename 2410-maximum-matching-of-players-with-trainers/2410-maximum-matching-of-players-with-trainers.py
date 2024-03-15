class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        matchings = 0
        j = 0

        for player in players:
            while j < len(trainers) and trainers[j] < player:
                j += 1
            if j < len(trainers):
                matchings += 1
                j += 1

        return matchings