def checkTie(board, player_1, player_2):
	for i in range(3):
		for j in range(3):
			if any([board[i][j] == player_1, board[i][j] == player_2]):
				pass
			else:
				return False
	return True
