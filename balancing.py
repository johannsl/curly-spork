from matchup import Matchup
from itertools import permutations

# PERMUTATIONS OF THE NUMBERS BETWEEN 1 AND 10 WILL BE CREATED
# 1-5 IS POSITIONS 1-5 FOR TEAM 1, 6-10 IS POSITION 1-5 FOR TEAM 2

def balance(players):
    best_score = 1000000
    best_matchup = None
    matchups = list(permutations(range(1, 11)))
    for matchup in matchups:
        new_matchup = Matchup(players, matchup)
        new_score = new_matchup.calculate_heuristic()
        if new_score < best_score:
            best_score = new_score
            best_matchup = new_matchup
            print("current best score: {}").format(best_score)
    return best_matchup
