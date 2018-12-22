import os
import file_handle
from player import Player
import balancing
from config import mmr_reduction_list, pos_reduction_list, heuristics_weights, player_rewards
import time
import json
from copy import deepcopy

player_list = []
lobby_list = []

def main():
    update_player_list()
    user_input()

def user_input():
    welcome = "WELCOME TO CURLY SPORK \n"
    commands = """commands: 
    add player
    remove player
    <playerindex> (adds / removes from lobby)
    balance
    print
    reset stats
    set config
    exit \n"""
    config = ("mmr_reduction_list = {}, pos_reduction_list = {}, heuristics_weights = {}, player_rewards = {} \t").format(
                mmr_reduction_list, pos_reduction_list, heuristics_weights, player_rewards)
    print(welcome)
    print(commands)
    print(config)

    while(1):
        print("\nplayer list: ")
        for index in range(len(player_list)):
            print("{0} \tName: {1:10} \tPositions: {2:20} \tExtern MMR: {3:10} " + \
                "\tIntern MMR: {4:10} \tDrafter: {5:10} \tWins: {6:5} \tLosses {7:5}").format(
                        index, 
                        player_list[index].name,
                        player_list[index].positions,
                        player_list[index].extern_mmr,
                        player_list[index].intern_mmr,
                        player_list[index].drafter,
                        player_list[index].wins,
                        player_list[index].losses
                        )

        print("\n")
        print("current lobby: {}\n").format(lobby_list)
        #os.system('clear')

        user_input = str(raw_input("$ "))

        if user_input == "exit":
            break

        elif user_input.startswith("add player"):
            name = str(raw_input("name: "))
            positions = str(raw_input("positions: "))
            mmr = str(raw_input("mmr: "))
            drafter = str(raw_input("drafter: "))
            new_player = Player(name, 
                                [int(x) for x in positions.split(" ")], 
                                int(mmr), 
                                0, 
                                int(drafter), 
                                0, 
                                0)
            player_list.append(new_player)
            file_handle.add_player(new_player)
            print("Player created! {}, {}, {}, {} \n").format(
                new_player.name,
                new_player.positions,
                new_player.extern_mmr,
                new_player.drafter)

        elif user_input.startswith("remove player"):
            name = str(raw_input("name: "))
            for player in player_list:
                if player.name == name:
                    player_list.remove(player)
                    file_handle.remove_player(player)
                    print("Player removed! {} \n").format(name)

        elif user_input.startswith("balance"):
            if len(lobby_list) < 10:
                print "too few people in lobby! \n"
                continue
            elif len(lobby_list) > 10:
                print "too many people in lobby! \n"
                continue
            drafters = 0
            for index in lobby_list:
                if player_list[index].drafter == 1:
                    drafters += 1
            if drafters < 2:
                print "too few drafters! \n"
                continue

            game_list = []
            for index in lobby_list:
                game_list.append(player_list[index])
            start = time.time()        
            matchup = balancing.balance(game_list)
            end = time.time()
            if matchup == None:
                print("No matchup found!")
                break
            matchup.get_teams()
            team_1 = matchup.team_1_players
            positions_1 = matchup.team_1_positions
            drafters_1 = matchup.team_1_drafters
            team_2 = matchup.team_2_players
            positions_2 = matchup.team_2_positions
            drafters_2 = matchup.team_2_drafters

            # PRINT THE DRAFT!
            print("Balancing took {} seconds").format(end - start)
            print("TEAM 1: \t\t{0:15} {1}, \t{2:15} {3}, \t{4:15} {5}, " + \
                "\t{6:15} {7}, \t{8:15} {9}").format(
                        team_1[0] + ":",
                        positions_1[0],
                        team_1[1] + ":",
                        positions_1[1],
                        team_1[2] + ":",
                        positions_1[2],
                        team_1[3] + ":",
                        positions_1[3],
                        team_1[4] + ":",
                        positions_1[4])
            print("TEAM 2: \t\t{0:15} {1}, \t{2:15} {3}, \t{4:15} {5}, " + \
                "\t{6:15} {7}, \t{8:15} {9}").format(
                        team_2[0] + ":",
                        positions_2[0],
                        team_2[1] + ":",
                        positions_2[1],
                        team_2[2] + ":",
                        positions_2[2],
                        team_2[3] + ":",
                        positions_2[3],
                        team_2[4] + ":",
                        positions_2[4]
                        )
            print("TEAM 1 DRAFTERS: \t{0:100}").format(json.dumps(drafters_1)) 
            print("TEAM 2 DRAFTERS: \t{0:100}").format(json.dumps(drafters_2)) 
            print("TEAM 1 MMR: \t\t{0} \tTEAM 1 POSITION OFFSET: \t{1}").format(
                    matchup.team_1_mmr, matchup.team_1_pos_offset)
            print("TEAM 2 MMR: \t\t{0} \tTEAM 2 POSITION OFFSET: \t{1}").format(
                    matchup.team_2_mmr, matchup.team_2_pos_offset)
            print("TOTAL POSITION OFFSET: \t{0} \t\tMMR DIFFERENCE: \t\t{1} \tTEAM POSITION OFFSET DIFFERENCE: \t{2}").format(
                    matchup.pos_offset,
                    abs(matchup.team_1_mmr - matchup.team_2_mmr),
                    abs(matchup.team_1_pos_offset - matchup.team_2_pos_offset))
            print("MATCHUP SCORE: \t\t{0} \n").format(matchup.score)

            winning_team = str(raw_input("which team won? \n"))
            if int(winning_team) == 1:
                for player in matchup.players:
                    if player.name in matchup.team_1_players:
                        player.win_match()
                    elif player.name in matchup.team_2_players:
                        player.lose_match()
            elif int(winning_team) == 2:
                for player in matchup.players:
                    if player.name in matchup.team_2_players:
                        player.win_match()
                    elif player.name in matchup.team_1_players:
                        player.lose_match()
            file_handle.save_match(matchup.players)

        elif user_input.startswith("print"):
            for index in range(len(player_list)):
                print("{0} \tName: {1:10} \tPositions: {2:20} \tDrafter: {3:10} \tWins: {4:5} ").format(
                            index, 
                            player_list[index].name,
                            player_list[index].positions,
                            player_list[index].drafter,
                            player_list[index].wins
                            )
            print("\n")
            print("current lobby: {}\n").format(lobby_list)

        elif user_input.startswith("reset stats"):
            dobble_check = str(raw_input("are you sure? \n"))
            if dobble_check == "y" or dobble_check == "yes":
                for player in player_list:
                    player.intern_mmr = 0
                    player.wins = 0
                    player.losses = 0
                file_handle.reset_stats(player_list)

        elif user_input.startswith("set config"):
            tot_pos_weight = float(raw_input("tot pos weight: "))
            mmr_diff_weight = float(raw_input("mrr diff weight: "))
            pos_diff_weight = float(raw_input("pos diff weight: "))
            heuristics_weights[0] = tot_pos_weight
            heuristics_weights[1] = mmr_diff_weight
            heuristics_weights[2] = pos_diff_weight

        else:
            try:
                val = int(user_input)
                if val < len(player_list) and val not in lobby_list:
                    lobby_list.append(val)
                else:
                    lobby_list.remove(val)
            except:
                config = ("mmr_reduction_list = {}, pos_reduction_list = {}, heuristics_weights = {}, player_rewards = {} \t").format(
                    mmr_reduction_list, pos_reduction_list, heuristics_weights, player_rewards)
                print(commands)
                print(config)
                continue

def update_player_list():
    players = file_handle.get_all_players()
    if players != {} and not player_list:
        for db_player in players:
            new_player = Player(
                players[db_player]["name"], 
                players[db_player]["positions"], 
                players[db_player]["extern_mmr"], 
                players[db_player]["intern_mmr"],
                players[db_player]["drafter"],
                players[db_player]["wins"],
                players[db_player]["losses"])
            player_list.append(new_player)
        print("playerlist in ram updated! \n")

if __name__ == "__main__":
    main()
