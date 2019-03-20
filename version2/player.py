from config import mmr_reduction_list, player_rewards

class Player:
    def __init__(self, name, positions, external_mmr, internal_mmr, drafter, 
                wins, losses):
        self.name = name
        self.positions = positions
        self.external_mmr = external_mmr
        self.internal_mmr = internal_mmr
        self.drafter = drafter
        self.wins = wins
        self.losses = losses
        self.mmr_list = self.calculate_mmr_list()

    def calculate_mmr_list(self):
        mmr_list = []
        for (index in range(self.positions)):
            mmr = self.total_mmr - (self.total_mmr * mmr_reduction_list[index])
            mmr_list.append(mmr)
        return mmr_list

    def total_mmr(self):
        return self.external_mmr + self.internal_mmr

    def total_matches(self):
        return self.wins + self.losses
    
    def win_match(self):
        if self.total_matches() == 0:
            self.internal_mmr += player_rewards[0]
        elif self.total_matches() == 1:
            self.internal_mmr += player_rewards[1]
        else:
            self.internal_mmr += player_rewards[2]
        self.mmr_list = self.calculate_mmr_list()
        self.wins += 1

    def lose_match(self):
        if self.total_matches() == 0:
            self.internal_mmr -= player_rewards[0]
        elif self.total_matches() == 1:
            self.internal_mmr -= player_rewards[1]
        else:
            self.internal_mmr -= player_rewards[2]
        self.mmr_list = self.calulate_mmr_list()
        self.losses += 1

