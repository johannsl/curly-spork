# THIS FILE IS A CONFIG
# IT STORES GLOBAL RUNTIME VARIABLES

# THESE SEEMINGLY RANDOM NUMBERS WERE CREATED BY A REAL STATISTICIAN, "DEEZ NUTZ"!
# they are the accumulative values of the serie 0 1 2 3 4
pos_reduction_list = [0, 1, 3, 6, 10]
mmr_reduction_list = [0, 0.01, 0.03, 0.06, 0.10] #%

# THESE ARE WEIGHTS FOR THE HEURISTICS FUNCTION
# they state that a total position offset of 4 is equally bad as
# a mmr difference of 250, or a position offset difference of 3
heuristics_weights = [25, 0.4, 33.3]

# THESE ARE PLAYER REWARDS
# first win is 100 points and so on
player_rewards = [100, 50, 25]

