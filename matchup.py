class Matchup:
    def __init__(self, players, positions):
        self.players = players
        self.positions = positions
        self.score = 0
        self.team_1 = {}
        self.team_2 = {}
        self.pos_offset = 0
        self.team_1_mmr = 0
        self.team_2_mmr = 0
        self.team_1_pos = 0
        self.team_2_pos = 0

    def calculate_heuristic(self):
        pos_offset = 0
        mmr_diff = 0
        pos_diff = 0
        
        for index in range(10):
            if self.positions[index] > 5:
                if self.positions[index]-5 in self.players[index].positions:
                    pos_offset += self.players[index].positions.index(self.positions[index]-5)
                    mmr_diff += self.players[index].extern_mmr + self.players[index].intern_mmr
                    pos_diff += self.players[index].positions.index(self.positions[index]-5)
                else:
                    self.score = 1000000
                    return self.score
            else:
                if self.positions[index] in self.players[index].positions:
                    pos_offset += self.players[index].positions.index(self.positions[index])
                    mmr_diff -= self.players[index].extern_mmr + self.players[index].intern_mmr
                    pos_diff -= self.players[index].positions.index(self.positions[index])
                else:
                    self.score = 1000000
                    return self.score
        
        self.score = pos_offset * 2.5 + abs(mmr_diff) + abs(pos_diff) * 33.3
        return self.score

    def get_teams(self):
        for index in range(10):
            if self.positions[index] > 5:
                self.team_2[self.players[index].name] = self.positions[index]-5
            else:
                self.team_1[self.players[index].name] = self.positions[index]
        
    def get_team_info(self):
        for index in range(10):
            if self.positions[index] > 5:
                if self.positions[index]-5 in self.players[index].positions:
                    self.pos_offset += self.players[index].positions.index(self.positions[index]-5)
                    self.team_2_mmr += self.players[index].extern_mmr + self.players[index].intern_mmr
                    self.team_2_pos += self.players[index].positions.index(self.positions[index]-5)
                else:
                    return False
            else:
                if self.positions[index] in self.players[index].positions:
                    self.pos_offset += self.players[index].positions.index(self.positions[index])
                    self.team_1_mmr += self.players[index].extern_mmr + self.players[index].intern_mmr
                    self.team_1_pos += self.players[index].positions.index(self.positions[index])
                else:
                    return False
        return True

