from config import mmr_reduction_list, pos_reduction_list, heuristics_weights

class Matchup:
    def __init__(self, players, positions):
        self.players = players
        self.positions = positions
        self.score = 0
        self.team_1_players = []
        self.team_1_positions = []
        self.team_2_players = []
        self.team_2_positions = []
        self.pos_offset = 0
        self.team_1_mmr = 0
        self.team_2_mmr = 0
        self.team_1_pos_offset = 0
        self.team_2_pos_offset = 0
        self.team_1_drafters = []
        self.team_2_drafters = []

    def calculate_heuristic(self):
        mmr_diff = 0
        pos_diff = 0

        for index in range(10):

            # TEAM 2
            if self.positions[index] > 5:
                if self.players[index].drafter == 1:
                    self.team_2_drafters.append(self.players[index].name)
                if self.positions[index]-5 in self.players[index].positions:
                    self.pos_offset += pos_reduction_list[self.players[index].positions.index(self.positions[index]-5)]
                    self.team_2_mmr += self.players[index].calculate_mmr_for_pos(self.positions[index]-5)
                    self.team_2_pos_offset += pos_reduction_list[self.players[index].positions.index(self.positions[index]-5)]
                else:
                    self.score = 1000000
                    return self.score
                    
            # TEAM 1
            else:
                if self.players[index].drafter == 1:
                    self.team_1_drafters.append(self.players[index].name)
                if self.positions[index] in self.players[index].positions:
                    self.pos_offset += pos_reduction_list[self.players[index].positions.index(self.positions[index])]
                    self.team_1_mmr += self.players[index].calculate_mmr_for_pos(self.positions[index])
                    self.team_1_pos_offset += pos_reduction_list[self.players[index].positions.index(self.positions[index])]
                else:
                    self.score = 1000000
                    return self.score
                     
        if not self.team_1_drafters and not self.team_2_drafters:
            self.score = 1000000
            return self.score
        
        mmr_diff = abs(self.team_1_mmr - self.team_2_mmr)
        pos_diff = abs(self.team_1_pos_offset - self.team_2_pos_offset)
        self.score = self.pos_offset * heuristics_weights[0] + \
                            mmr_diff * heuristics_weights[1] + \
                            pos_diff * heuristics_weights[2]
        return self.score

    def get_teams(self):
        for index in range(10):

            # TEAM 2
            if self.positions[index] > 5:
                self.team_2_players.append(self.players[index].name)
                self.team_2_positions.append(self.positions[index]-5)

            # TEAM 1
            else:
                self.team_1_players.append(self.players[index].name)
                self.team_1_positions.append(self.positions[index])
        
