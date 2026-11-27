class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score_call_equal_scores(self):
        score_calls = {0: "Love-All", 1: "Fifteen-All", 2: "Thirty-All"}
        score = score_calls[self.m_score1] if self.m_score1 in score_calls else "Deuce" 
        return score

    def get_score_big_score(self):
        score_difference = self.m_score1 - self. m_score2
        if score_difference < -2: score_difference = -2
        if score_difference > 2: score_difference = 2
        score_calls = {1: "Advantage player1", -1: "Advantage player2", 2: "Win for player1", -2: "Win for player2"}
        return score_calls[score_difference]
    
    def get_score_other_cases(self):
        score_calls = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        player1_score = score_calls[self.m_score1]
        player2_score = score_calls[self.m_score2]
        return  player1_score + "-" + player2_score

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.get_score_call_equal_scores()

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.get_score_big_score()

        return self.get_score_other_cases()
