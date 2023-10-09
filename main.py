import os
import time

from lib import TicTac,winPos, circular_list

tt = TicTac()

player_1 = tt.player_1
player_2 = tt.player_2

score = {player_1: 0, player_2: 0}

get_players = circular_list.run(player_1, player_2)

def positioning():
	pos = {}
	tmp = 1
	for i in range(3):
		for j in range(3):
			pos[f"{tmp}"] = (i,j)
			tmp += 1
	return pos

while True:
	print()

	print(f"{player_1} {score[player_1]}:{score[player_2]} {player_2}")

	tt.printBoard()
	player = get_players.data
	print(
		"To play enter the pos number from" \
		"\t1 - 9"
	)

	play = input(f"{player} - ")
	if play.lower().strip() == 'exit' or play.lower().strip() == 'quit':
		print("Y O U  E N D E D  T H E  G A M E!!!")
		break
	if play in [str(i) for i in range(1, 10)]:
		pos_x, pos_y = positioning()[play]
		tt.move(player, pos_x, pos_y)
	if tt.isWin(player):
		score[player] += 1

		tt = TicTac()
		print("N E X T  GAME S T A R T  S O O N ! ! !")
		time.sleep(2)
		os.system("clear")
		continue
	else:
		time.sleep(1)
		os.system("clear")

	get_players = get_players.next
