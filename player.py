from config import mmr_reduction_list, player_rewards

class Player:
    def __init__(self, name, positions, 
                    extern_mmr, intern_mmr, drafter, wins, losses):
        self.name = name
        self.positions = positions
        self.extern_mmr = extern_mmr
        self.intern_mmr = intern_mmr
        self.drafter = drafter
        self.wins = wins
        self.losses = losses

    def calculate_mmr_for_pos(self, position):
        base_mmr = self.extern_mmr + self.intern_mmr
        mmr = base_mmr - (base_mmr * mmr_reduction_list[self.positions.index(position)])
        return mmr
    
    def win_match(self):
        if self.wins + self.losses == 0:
            self.intern_mmr += player_rewards[0]
        elif self.wins + self.losses == 1:
            self.intern_mmr += player_rewards[1]
        else:
            self.intern_mmr += player_rewards[2]
        self.wins += 1

    def lose_match(self):
        if self.wins + self.losses == 0:
            self.intern_mmr -= player_rewards[0]
        elif self.wins + self.losses == 1:
            self.intern_mmr -= player_rewards[1]
        else:
            self.intern_mmr -= player_rewards[2]
        self.losses += 1

