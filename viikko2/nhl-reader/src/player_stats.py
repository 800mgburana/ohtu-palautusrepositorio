class PlayerStats:
    def __init__(self, players):
        self._players = players

    def top_by_nationality(self, nationality):
        result = {}

        for player in self._players:
            if player.nationality == nationality:
                result[str(player)] = player.total

        result = sorted(result.items(), key=lambda x:x[1], reverse=True)
        result = [x[0] for x in result]
        return result
