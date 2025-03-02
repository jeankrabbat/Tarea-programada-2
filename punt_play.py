class Punt_Play:
    def __init__(self, game_id, teams, total_yards, quarter):
        self.game_id = game_id
        self.teams = teams
        self.total_yards = total_yards
        self.quarter = quarter

    def __eq__(self, other):
        return self.total_yards == other.total_yards
    
    def __lt__(self, other):
        return self.total_yards < other.total_yards

    def __gt__(self, other):
        return self.total_yards > other.total_yards

    def __le__(self, other):
        return self.total_yards <= other.total_yards

    def __ge__(self, other):
        return self.total_yards >= other.total_yards