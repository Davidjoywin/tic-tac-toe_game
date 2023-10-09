from .get_win_pos import winPos


class TicTac:
	def __init__(self):
		self.board = [['-' for _ in range(3)] for _ in range(3)]
		self.player_1 = 'X'
		self.player_2 = 'O'

	def move(self, player, x, y):
		if self.board[x][y] != self.player_1 and \
			self.board[x][y] != self.player_2:
	
			self.board[x][y] = player
		else:
			print("Invalid POS")

		self.printBoard()
		if self.isWin(player):
			print(f"{player}: Congratulation, you won")

	def isWin(self, player):
		win_pos = winPos()
		for pos in win_pos:

			# get the boolean value if the cell is filled
			# by a player or not
			player_pos = []
			for x, y in pos:
				check = self.board[x][y] == player
				player_pos.append(check)
			is_win = all(player_pos)

			if not is_win:
				continue
			else:
				return is_win
		return False

	def printBoard(self):
		print(end="\v")
		for i in range(3):
			print(end="\t")
			for j in range(3):
				print(f"{self.board[i][j]}", end='')
				if j < 2:
					print("\t", end='')
			if i < 2:
				print("\v")
			print()
