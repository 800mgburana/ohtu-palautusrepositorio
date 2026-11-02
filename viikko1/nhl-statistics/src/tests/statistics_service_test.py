import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_okname(self):
        result = self.stats.search("Semenko")
        self.assertEqual(str(result), "Semenko EDM 4 + 12 = 16")

    def test_wrongname(self):
        result = self.stats.search("nfjiasfolaaf,oao,voa")
        self.assertEqual(result, None)

    def test_team(self):
        result = self.stats.team("PIT")
        correct = "Lemieux PIT 45 + 54 = 99"
        self.assertEqual(str(result[0]), correct)

    def test_top(self):
        result = self.stats.top(1)
        correct = "Gretzky EDM 35 + 89 = 124"
        self.assertEqual(str(result[0]), correct)

    def test_sortby_goals(self):
        result = self.stats.top(1, SortBy.GOALS)
        correct = "Lemieux PIT 45 + 54 = 99"
        self.assertEqual(str(result[0]), correct)

    def test_sortby_assists(self):
        result = self.stats.top(1, SortBy.ASSISTS)
        correct = "Gretzky EDM 35 + 89 = 124"
        self.assertEqual(str(result[0]), correct)