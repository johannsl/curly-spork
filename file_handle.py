import json
import os

def get_all_players():
    try:
        check_if_empty("players.json")
        with open("players.json", "r") as f:
            data = json.load(f)
            return data["players"]
    except:
        print("get_all_players failed! \n")
    

def add_player(new_player):
    try:
        check_if_empty("players.json")
        with open("players.json", "r") as f:
            data = json.load(f)
            data["players"][new_player.name] = {
                "name": new_player.name, 
                "positions": new_player.positions,
                "extern_mmr": new_player.extern_mmr,
                "intern_mmr": new_player.intern_mmr,
                "drafter": new_player.drafter,
                "wins": new_player.wins,
                "losses": new_player.losses
            }
        with open("players.json", "w") as f:
            json.dump(data, f)
    except:
        print("add_player failed! \n")

def remove_player(del_player):
    try:
        check_if_empty("players.json")
        with open("players.json", "r") as f:
            data = json.load(f)
            for player in data["players"]:
                if player == del_player.name:
                    del data["players"][player]
                    break
        with open("players.json", "w") as f:
            json.dump(data, f)
    except:
        print("remove_player failed! \n")

def check_if_empty(file):
    try:
        if (not os.path.isfile(file)):
            print("file not found! \n")
            with open(file, "w") as f:
                json.dump({"players": {}}, f)
    except:
        print("check_if_empty failed! \n")

def save_match(players):
    try:
        check_if_empty("players.json")
        with open("players.json", "r") as f:
            data = json.load(f)
            for player in players:
                data["players"][player.name]["intern_mmr"] = player.intern_mmr
                data["players"][player.name]["wins"] = player.wins
                data["players"][player.name]["losses"] = player.losses
        with open("players.json", "w") as f:
            json.dump(data, f)
    except:
        print("save_match failed! \n")

def reset_stats(players):
    try:
        check_if_empty("players.json")
        with open("players.json", "r") as f:
            data = json.load(f)
            for player in players:
                data["players"][player.name]["intern_mmr"] = 0
                data["players"][player.name]["wins"] = 0
                data["players"][player.name]["losses"] = 0
        with open("players.json", "w") as f:
            json.dump(data, f)
    except:
        print("reset_intern_mmr failed! \n")

