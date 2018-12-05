from config import mmr_reduction_list

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

