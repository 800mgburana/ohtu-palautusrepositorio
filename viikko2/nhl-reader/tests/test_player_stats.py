import unittest

from src.player_stats import PlayerStats


class FakePlayer:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = str(goals)
        self.assists = str(assists)
        self.total = goals + assists

    def __str__(self):
        return self.name


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.players = [
            FakePlayer("Alex", "FIN", "AAA", 20, 30),
            FakePlayer("Blake", "USA", "BBB", 35, 10),
            FakePlayer("Casey", "FIN", "AAA", 15, 25),
            FakePlayer("Drew", "CAN", "AAA", 10, 20),
        ]
        self.stats = PlayerStats(self.players)

    def test_top_by_nationality_returns_matching_players_by_points(self):
        self.assertEqual(
            self.stats.top_by_nationality("FIN"),
            ["Alex", "Casey"],
        )

    def test_top_by_nationality_returns_empty_list_when_no_players_match(self):
        self.assertEqual(self.stats.top_by_nationality("SWE"), [])

    def test_top_goal_scorers_returns_only_top_x_players(self):
        self.assertEqual(
            self.stats.top_goal_scorers(2),
            [self.players[1], self.players[0]],
        )

    def test_top_goal_scorers_returns_all_players_when_x_is_larger(self):
        self.assertEqual(
            self.stats.top_goal_scorers(10),
            [self.players[1], self.players[0], self.players[2], self.players[3]],
        )

    def test_top_by_team_returns_matching_players_by_points(self):
        self.assertEqual(
            self.stats.top_by_team("AAA"),
            [self.players[0], self.players[2], self.players[3]],
        )

    def test_top_by_team_returns_empty_list_when_no_players_match(self):
        self.assertEqual(self.stats.top_by_team("CCC"), [])


if __name__ == "__main__":
    unittest.main()
