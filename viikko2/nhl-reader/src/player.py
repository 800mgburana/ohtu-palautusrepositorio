class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.total = int(self.assists) + int(self.goals)
        self.team = dict['team']
        self.games = dict['games']

    def __str__(self):
        return f'''{self.nationality} {self.name} team {self.team} 
        | {self.games} games, {self.assists} + {self.goals} = {self.total}'''
