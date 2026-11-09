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

    def top_goal_scorers(self, x):
        """Return the top x players sorted by number of goals, highest first."""
        players = sorted(self._players, key=lambda player: int(player.goals), reverse=True)
        return players[:x]

    def top_by_team(self, team):
        """Return players from the given team sorted by points, highest first."""
        players = [player for player in self._players if player.team == team]
        return sorted(players, key=lambda player: player.total, reverse=True)
