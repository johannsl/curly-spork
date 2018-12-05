import os
import file_handle
from player import Player
import balancing
from config import mmr_reduction_list, pos_reduction_list, heuristics_weights

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
    exit \n"""
    config = ("mmr_reduction_list = {} \tpos_reduction_list = {} \theuristics_weights = {} \t").format(
        mmr_reduction_list, pos_reduction_list, heuristics_weights)
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
            matchup = balancing.balance(game_list)
            matchup.get_teams()
            print("TEAM 1: \t{} \tTEAM 2: \t{}").format(matchup.team_1, matchup.team_2)
            print("MATCHUP SCORE: \t{}").format(matchup.score)
            if not matchup.get_team_info():
                print("something went wrong with the matchup! \n")
            print("TEAM 1 HAS: \t{} mmr \t{} position offset " + \
                    "\tTEAM 2 HAS: \t{} mmr\t{} position offset").format(
                    matchup.team_1_mmr, matchup.team_1_pos,
                    matchup.team_2_mmr, matchup.team_2_pos)
            print("TOTAL OFFSET IS: {} \tMMR DIFFERENCE IS: {}\t OFFSET DIFFERENCE IS: {}\n").format(
                    matchup.pos_offset, 
                    abs(matchup.team_1_mmr - matchup.team_2_mmr),
                    abs(matchup.team_1_pos - matchup.team_2_pos))

        else:
            try:
                val = int(user_input)
                if val < len(player_list) and val not in lobby_list:
                    lobby_list.append(val)
                else:
                    lobby_list.remove(val)
            except:
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
