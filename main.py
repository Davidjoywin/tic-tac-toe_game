import os
import time

from ai import Agent
from lib import positioning
from lib import score as scoreStorage
from lib import TicTac, checkTie, circular_list
from lib import chooseMode, getHelp


tt = TicTac()
agent = Agent()

player_1 = tt.player_1
player_2 = tt.player_2

score = {player_1: 0, player_2: 0}

players_mode = {player_1: None, player_2: None}

get_players = circular_list.run(player_1, player_2)

position = positioning()


while True:
    # Before match starts
    if not any(players_mode.values()):
        # if any the players mode is not assigned a mode
        try:
            chooseMode(players_mode)
        except Exception:
            continue

    # After match starts
    print()

    print(f"{player_1} {score[player_1]}:{score[player_2]} {player_2}")

    tt.printBoard()
    player = get_players.data

    print(
            "To play enter the pos number from" \
            "\t1 - 9"
        )
    
    play = ''
    if players_mode[player] == 'real':
        play = input(f"{player} - ")

    else:
        agent.buildWeight(tt.board, player, ('X', 'O'))
        play = agent.getBestMove()
        for key, value in position.items():
            if value == play:
                play = key
                break

    if play.lower().strip() == 'exit' or play.lower().strip() == 'quit':
        scoreStorage(score)
        print("Y O U  E N D E D  T H E  G A M E!!!")
        break

    if play in [str(i) for i in range(1, 10)]:
        pos_x, pos_y = position[play]
        tt.move(player, pos_x, pos_y)

    if tt.isWin(player):
        score[player] += 1

        tt = TicTac()
        print("N E X T  G A M E  S T A R T  S O O N ! ! !")
        time.sleep(2)
        os.system("clear")
        continue

    elif checkTie(tt.board, player_1, player_2):
        tt = TicTac()
        print("M A T C H  T I E! ! !")
        time.sleep(2)
        os.system("clear")
        continue

    else:
        time.sleep(1)
        os.system("clear")

    get_players = get_players.next
