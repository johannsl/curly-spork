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

