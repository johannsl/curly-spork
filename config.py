# THIS FILE IS A CONFIG
# IT STORES GLOBAL RUNTIME VARIABLES

# THESE SEEMINGLY RANDOM NUMBERS WERE CREATED BY A REAL STATISTICIAN, "DEEZ NUTZ"!
# they are the accumulative values of the serie 0 1 2 3 4
pos_reduction_list = [0, 1, 3, 6, 10]
mmr_reduction_list = [0, 0.01, 0.03, 0.06, 0.10] #%

# THESE ARE WEIGHTS FOR THE HEURISTICS FUNCTION
# they are based on the belief that
# 40 total position offset is equal to
# 100 mmr difference is equal to
# 3 team position offset
heuristics_weights = [5, 1, 33.33]

# THESE ARE PLAYER REWARDS
# first win is 100 points and so on
# maybe this will make the balancing process more robust?
player_rewards = [100, 50, 25]

