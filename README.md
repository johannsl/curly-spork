# curly-spork aka TAWsome lobbymaker
DotA 2 lobby balancing command line interface

*would you ever go as far as even?*

## Get started
  1. you clone this repo
  2. you get python 2
  3. you run python main.py
  4. you add players
  5. you write balance
  6. ?????
  7. profit

## Contribution
I will probably not work on this for a while since version 1 seems quite stable. Feel free to create pull requests, or contact me if you wanna contribute on this repo directly.

## Suggestions for improvement
* Very high mmr player should not play mid or carry;
* Very high mmr players should be divided on similar positions / lanes. If both teams got a very high mmr player, they should for example not be placed on support (position 5) and carry (position 1);
* The player list should stay in the same order (not change when you restar program / add new player);
* The win / loss bonus should probaby be reset from [100, 50, 25] to a constant 50;
* What position a player plays could affect their mmr, for example by position [1, 2, 3, 4, 5] to a bonus of [10%, 6%, 3%, 1%, 0%] mmr. This would make high mmr players playing carry to get a higher bonus than a low mmr player playing carry, and thus be better balanced. It is probably not beneficial to have a high mmr carry on one team and a low mmr carry on the other.

## Credits
Thanks to Deez Nutz for input on the nature of mmr from a statisticians point of view

Thanks to Zenotha for this article on mmr https://www.reddit.com/r/DotA2/comments/2dfjge/reverseengineering_the_effects_of_average_team/

## Example images
### Start program
![Start program](./images/start_program2.png?raw=true "Start program")
### Add player to storage
![Add player to storage](./images/add_player_to_storage.png?raw=true "Add player to storage")
### Add player to lobby
![Add player to lobby](./images/add_player_to_lobby.png?raw=true "Add player to lobby")
### Balance lobby
![Balance lobby](./images/balance_lobby.png?raw=true "Balance lobby")
### Record winning team
![Record winning team](./images/record_winning_team.png?raw=true "Record winning team")
