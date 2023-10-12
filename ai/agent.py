from lib import winPos


class Agent:
	def __init__(self):
		self.weight = {}

	def buildWeight(self, board):
		win_pos = winPos()
		for i in range(3):
			for j in range(3):
				pos = (i, j)
				is_visited = pos in visited

	@staticmethod
	def getPotMove(board, pos, player_1, player_2):
		"""
		getPotMove: get potential/possible best moves of a player
		
		return: list of win-pos (win-pos is a list of potential win in tuple(x,y))
		"""

		x, y = pos
		if board[x][y] == player_1 or board[x][y] == player_2:
			return None

		else:
			pot = []
			for win_pos in winPos():
				if pos in win_pos:
					pot.append(win_pos)
			return pot

	@staticmethod
	def joinPotMovesSides(potMoves, cur_pos):
		pos_list = []
		for pos in pot:
			pos_list.append(pos)
		
		# join all the win pos together in a list and
		# exempt the pos whose weight is being computed

		return list(filter(
			pos_list, lambda val: if val == cur_pos
		))

	def assignWeight(board, cur_pos, potMoves, player_1, player_2):
		
		for pos in potMoves:
			x, y = pos
			
