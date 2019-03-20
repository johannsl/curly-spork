from cmd import Cmd

from printer import welcome

def rehydrate_player_list():
     storage_players = file_handle.get_all_players()
     if players != {} and not player_list:
         for player in storage_players:
             new_player = Player(
                 storage_players[db_player]["name"],
                 players[db_player]["positions"],
                 players[db_player]["extern_mmr"],
                 players[db_player]["intern_mmr"],
                 players[db_player]["drafter"],
                 players[db_player]["wins"],
                 players[db_player]["losses"])
             player_list.append(new_player)
         print("playerlist in ram updated! \n")

class CurlySpork(Cmd):
    player_list = []
    lobby_list = []
     
    def do_ap(self, args):
        "Adds a player to the storage. The command requires: player name, " \
        "player preferred positions (in order), player mmr, and if the player " \
        "can draft.\n" \
        "Example: ap OrangePlus 1 2 3 4 5 9001 yes\n"

    def do_rp(self, args):
        "Removes a player from the storage. The command requires a player's " \
        "name.\n" \
        "Example: rp OrangePlus\n"

    def do_balance(self, args):
        "Creates two balanced teams based on ten players in the lobby list\n"

    def do_print(self, args):
        "Prints the storage information excluding info on mmr and losses\n"

    def do_rs(self, args):
        "Resets the player stats in the storage. The player stats are wins, " \
        "losses, and the associated internal mmr\n"

    def do_sc(self, args):
        "Sets the configuration weights. There are three weights: one " \
        "concerning the total position offset, a second concerning the mmr " \
        "difference and a third concerning the team difference in position " \
        "offset. The command requires a value for each of these weights.\n" \
        "Example: sc 25 0.4 33.3\n"

    def do_quit(self, args):
        "Quits the program\n"
        print("Quitting")
        raise SystemExit

    def emptyline(self):
        return

    def precmd(self, line):
        print("LOL")
        line = line.lower()
        return line

    def postcmd(self, stop, line):
        print("LOL3")
        return stop 

    def preloop(self):
        print("LOL2")

if __name__ == "__main__":
    prompt = CurlySpork()
    prompt.prompt = "> "
    prompt.cmdloop(welcome())

