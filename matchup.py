from config import mmr_reduction_list, pos_reduction_list, heuristics_weights

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
        drafter_team_1 = False
        drafter_team_2 = False

        for index in range(10):
            if self.positions[index] > 5:
                if self.players[index].drafter == 1:
                    drafter_team_2 = True
                if self.positions[index]-5 in self.players[index].positions:
                    pos_offset += pos_reduction_list[self.players[index].positions.index(self.positions[index]-5)]
                    mmr_diff += self.players[index].calculate_mmr_for_pos(self.positions[index]-5)
                    pos_diff += pos_reduction_list[self.players[index].positions.index(self.positions[index]-5)]
                else:
                    self.score = 1000000
                    return self.score
            else:
                if self.players[index].drafter == 1:
                    drafter_team_1 = True
                if self.positions[index] in self.players[index].positions:
                    pos_offset += pos_reduction_list[self.players[index].positions.index(self.positions[index])]
                    mmr_diff -= self.players[index].calculate_mmr_for_pos(self.positions[index])
                    pos_diff -= pos_reduction_list[self.players[index].positions.index(self.positions[index])]
                else:
                    self.score = 1000000
                    return self.score
                     
        if not drafter_team_1 and not drafter_team_2:
            self.score = 1000000
            return self.score

        self.score = pos_offset * heuristics_weights[0] + \
                        abs(mmr_diff) * heuristics_weights[1] + \
                        abs(pos_diff) * heuristics_weights[2]
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

