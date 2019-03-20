import json
import os

def get_all_players():
    try:
        check_if_empty("players.json")
        with open("players.json", "r") as f:
            data = json.load(f)
            return data["players"]
    except:
        print("STORAGE.PY: GET_ALL_PLAYERS() FAILED! \n")
    

def add_player(new_player):
    try:
        check_if_empty("players.json")
        with open("players.json", "r") as f:
            data = json.load(f)
            data["players"][new_player.name] = {
                "name": new_player.name, 
                "positions": new_player.positions,
                "external_mmr": new_player.external_mmr,
                "internal_mmr": new_player.internal_mmr,
                "drafter": new_player.drafter,
                "wins": new_player.wins,
                "losses": new_player.losses
            }
        with open("players.json", "w") as f:
            json.dump(data, f)
    except:
        print("STORAGE.PY: ADD_PLAYER() FAILED! \n")

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
        print("STORAGE.PY: REMOVE_PLAYER() FAILED! \n")

def check_if_empty(file):
    try:
        if (not os.path.isfile(file)):
            print("STORAGE.PY: STORAGE FILE NOT FOUND! \n")
            with open(file, "w") as f:
                json.dump({"players": {}}, f)
    except:
        print("STORAGE.PY: CHECK_IF_EMPTY() FAILED! \n")

def save_match(players):
    try:
        check_if_empty("players.json")
        with open("players.json", "r") as f:
            data = json.load(f)
            for player in players:
                data["players"][player.name]["internal_mmr"] = player.internal_mmr
                data["players"][player.name]["wins"] = player.wins
                data["players"][player.name]["losses"] = player.losses
        with open("players.json", "w") as f:
            json.dump(data, f)
    except:
        print("STORAGE.PY: SAVE_MATCH() FAILED! \n")

def reset_stats(players):
    try:
        check_if_empty("players.json")
        with open("players.json", "r") as f:
            data = json.load(f)
            for player in players:
                data["players"][player.name]["internal_mmr"] = 0
                data["players"][player.name]["wins"] = 0
                data["players"][player.name]["losses"] = 0
        with open("players.json", "w") as f:
            json.dump(data, f)
    except:
        print("STORAGE.PY: RESET_STATS() FAILED! \n")

