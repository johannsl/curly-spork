import os
import file_handle
from player import Player

player_list = []
lobby_list = []

def main():
    print("Hello World")
    update_player_list()
    user_input()

def user_input():
    welcome = "WELCOME TO CURLY SPORK \n"
    commands = """commands: 
    add player
    remove player
    <playerindex> (adds / removes from lobby)
    exit \n"""
    print(welcome)
    print(commands)

    while(1):
        print("\nplayer list: ")
        for index in range(len(player_list)):
            print("{0} \tName: {1:10} \tPositions: {2:40} \tExtern MMR: {3:10} " + \
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
        print("current lobby: {} \n").format(lobby_list)
        #os.system('clear')

        user_input = str(raw_input("$ "))

        if user_input == "exit":
            break

        elif user_input.startswith("add player"):
            name = str(raw_input("name: "))
            positions = str(raw_input("positions: "))
            mmr = str(raw_input("mmr: "))
            drafter = str(raw_input("drafter: "))
            new_player = Player(name, positions.split(" "), int(mmr), 0, bool(drafter), 0, 0)
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
